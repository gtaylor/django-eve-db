"""
This module holds all importer related classes.
"""

class SQLImporter(object):
    """
    Serves as the encapsulating class for importers.
    """
    # A list of other table names that this class depends on (strings).
    DEPENDENCIES = []
    
    def run_importer(self):
        """
        This needs to be over-ridden on all sub-classes!
        """
        pass
    
    def parse_int_bool(self, int_bool):
        """
        Takes an int and converts it to a bool in the basis of 1=True, 0=False.
        """
        if int_bool == 1:
            return True
        else:
            return False