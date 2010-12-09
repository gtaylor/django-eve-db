"""
This module holds all importer related classes.
"""
from progressbar import ProgressBar, Percentage, Bar, ETA
from django import db
from django.db import transaction
from django.conf import settings
from eve_db.ccp_importer.bulkops import insert_many, update_many

class SQLImporter(object):
    """
    Serves as the encapsulating class for importers.
    """
    # A list of other table names that this class depends on (strings).
    DEPENDENCIES = []
    model = None
    # A mapping of model primary keys to CCP dump primary keys
    # For multi-column PKs this is not actually the true Django PK but the 
    # fields (presumably unique_together) that map to the CCP multi-column PKs! 
    pks = ()
    # A mapping of model fields to CCP dump columns. Without previously
    # specified PK fields!
    field_map = ()

    def __init__(self):
        self.insert_only = False
        self.cursor = None
        self.table_name = self.get_importer_name()
        self.row_count = 0
        self.itercount = 0
        self.progress_update_interval = 0
        self.pbar = None

    @transaction.commit_manually
    def prep_and_run_importer(self, conn):
        """
        Prepares the SQLite objects, progress bars, and other things and
        runs the importer.
        """
        self.cursor = conn.cursor()
        # Right now, the importer name matches the table name.
        self._setup_progressbar()
        self.insert_only = self.model.objects.all().count() == 0

        transaction.commit()

        inserts_bucket = []
        updates_bucket = []
        inserts_counter = 0
        updates_counter = 0
        batch_size = 1000
        self.itercount = 0
        query_string = 'SELECT * FROM %s' % self.table_name

        try:
            for new_obj, insert in (self.import_row(row) for row in self.cursor.execute(query_string)):
                # Now we have either a new model instance, an existing model
                # instance with updated fields or None == skip
                if new_obj:
                    if insert:
                        inserts_bucket.append(new_obj)
                        inserts_counter += 1
                        if inserts_counter % batch_size == 0:
                            insert_many(inserts_bucket)
                            inserts_bucket = []
                    else:
                        updates_bucket.append(new_obj)
                        updates_counter += 1
                        if updates_counter % batch_size == 0:
                            update_many(updates_bucket)
                            updates_bucket = []

                if self.itercount % self.progress_update_interval == 0:
                    self._progress_handler()

                self.itercount += 1

    #                if settings.DEBUG:
    #                    db.reset_queries()
            if len(inserts_bucket) > 0:
                insert_many(inserts_bucket)
            if len(updates_bucket) > 0:
                update_many(updates_bucket)
        except Exception:
            transaction.rollback()
            raise
        else:
            transaction.commit()
        # Progressbar to 100%.
        self.pbar.finish()
        # Clean up the cursor, free the memory.
        self.cursor.close()

    def import_row(self, row):
        row_params = self._get_fields_param_dict(row)
        pk_params_get = self._get_pk_param_dict(row)
        pk_params_insert = self._get_pk_param_dict(row, suffix='_id')
        if self.insert_only:
            # When creating a new instance we want both PK params and row params
            return self.model(**dict(pk_params_insert, **row_params)), True

        try:
            old_instance = self.model.objects.get(**pk_params_get)
        except self.model.DoesNotExist:
            return self.model(**dict(pk_params_insert, **row_params)), True
        else:
            # If we don't have any fields that need to be updated,
            # we should just skip an update.
            if row_params == {}:
                return None, None
            # Update fields and return the instance for updating
            for field_name, value in row_params.items():
                setattr(old_instance, field_name, value)
            return old_instance, False

    def _get_fields_param_dict(self, row):
        param_dict = {}
        for field_info in self.field_map:
            if len(field_info) == 3:
                model_field, import_field, convert_func = field_info
                param_dict[model_field] = convert_func(row[import_field])
            else:
                model_field, import_field = field_info
                param_dict[model_field] = row[import_field]
        return param_dict

    def _get_pk_param_dict(self, row, suffix=''):
        pk_param_dict = {}
        apply_suffix = True
        for field_info in self.pks:
            if len(field_info) == 3:
                model_field, import_field, apply_suffix = field_info
            else:
                model_field, import_field = field_info

            if model_field == self.model._meta.pk.column or not apply_suffix:
                pk_param_dict[model_field] = row[import_field]
            else:
                pk_param_dict["%s%s" % (model_field, suffix)] = row[import_field]
        return pk_param_dict

    def _setup_progressbar(self):
        """
        Instantiates and configures the ProgressBar for the importer.
        """
        count_query_string = 'SELECT count(*) AS count from %s' % self.table_name
        # Count the rows in the table.
        self.row_count = self.cursor.execute(count_query_string).fetchone()['count']
        # Every N number of iterations, update the progress bar. Do this
        # relative to query size.
        self.progress_update_interval = max(1, self.row_count / 100)
        # No more than 1000. Give the user more frequent updates.
        self.progress_update_interval = min(500, self.progress_update_interval)

        bar_label = " - %s: " % self.table_name
        widgets = [bar_label,
                   Percentage(), ' ', Bar(marker='=', left='[', right=']'),
                   ' ', ETA()]
        self.pbar = ProgressBar(widgets=widgets, maxval=self.row_count)
        self.pbar.start()

    def _progress_handler(self):
        """
        Updates the progress bar based on the current row being imported
        in the SQLite queryset. Called at intervals relative to query size.
        """
        self.pbar.update(self.itercount)

    def get_importer_name(self):
        """
        Returns the name of the importer. Currently, this is just the
        table name.
        """
        return self.__class__.__name__.split('_')[1]


def parse_int_bool(int_bool):
    """
    Takes an int and converts it to a bool in the basis of 1=True, 0=False.
    """
    if int_bool == 1:
        return True
    return False

def parse_char_notnull(value):
    '''
    Takes a nullable char and converts it to empty char if null
    '''
    if value is not None:
        return value
    return ''
