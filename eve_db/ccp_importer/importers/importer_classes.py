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
    # Django does not support multi-column PKs but you still need to
    # specify each field that maps to multi-column PKs! 
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
        prepare_func = self.import_row
        if self.insert_only:
            prepare_func = self.import_new_row
        
        transaction.commit()
        
        inserts_bucket = []
        updates_bucket = []
        inserts_counter = 0
        updates_counter = 0
        batch_size = 1000
        self.itercount = 0
        query_string = 'SELECT * FROM %s' % self.table_name
        
        try:
            for new_obj, insert in (prepare_func(row) for row in self.cursor.execute(query_string)):
                # Import the row as per the sub-classes import_row().
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

#    def import_row(self, row):
#        """
#        This needs to be over-ridden on all sub-classes!
#        """
#        raise NotImplementedError
    
    def import_row(self, row):
        row_params = self._get_row_param_dict(row, self.field_map)
        pk_params = self._get_row_param_dict(row, self.pks)
        row_params.update(pk_params)
        new_instance = self.model(**row_params)
        if self.insert_only:
            return new_instance, True
        
        try:
            old_instance = self.model.objects.get(**pk_params)
            for field_name, value in row_params.items():
                setattr(old_instance, field_name, value)
            return old_instance, False
        except self.model.DoesNotExist:
            return new_instance, True
        
    def _get_row_param_dict(self, row, field_list):
        param_dict = {}
        for model_field, import_field in field_list:
            param_dict[model_field] = row[import_field]
        return param_dict
            
    
    def import_new_row(self, row):
        '''
        Inserts a row from CCP dump. We do not query for existing record.
        This is not really needed on *every* importer so if it's not defined on 
        subclasses we'll just call import_row 
        '''
        return self.import_row(row)

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

    def parse_int_bool(self, int_bool):
        """
        Takes an int and converts it to a bool in the basis of 1=True, 0=False.
        """
        if int_bool == 1:
            return True
        else:
            return False

    def get_importer_name(self):
        """
        Returns the name of the importer. Currently, this is just the
        table name.
        """
        return self.__class__.__name__.split('_')[1]
