"""
This module holds all importer related classes.
"""
from progressbar import ProgressBar, Percentage, Bar, ETA
from django import db
from django.db import transaction
from django.conf import settings

class SQLImporter(object):
    """
    Serves as the encapsulating class for importers.
    """
    # A list of other table names that this class depends on (strings).
    DEPENDENCIES = []

    @transaction.commit_manually
    def prep_and_run_importer(self, conn):
        """
        Prepares the SQLite objects, progress bars, and other things and
        runs the importer.
        """
        self.cursor = conn.cursor()
        # Right now, the importer name matches the table name.
        self.table_name = self.get_importer_name()
        self._setup_progressbar()
        transaction.commit()
        
        try:
            self.itercount = 0
            query_string = 'SELECT * FROM %s' % self.table_name
            for row in self.cursor.execute(query_string):
                # Import the row as per the sub-classes import_row().
                self.import_row(row)
                if self.itercount % self.progress_update_interval == 0:
                    self._progress_handler()
    
                self.itercount += 1
                if settings.DEBUG:
                    db.reset_queries()
        except Exception:
            transaction.rollback()
            raise
        else:
            transaction.commit()
        # Progressbar to 100%.
        self.pbar.finish()
        # Clean up the cursor, free the memory.
        self.cursor.close()

    @transaction.commit_manually
    def import_row(self, row):
        """
        This needs to be over-ridden on all sub-classes!
        """
        pass

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
