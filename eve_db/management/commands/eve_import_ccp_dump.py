from django.core.management.base import BaseCommand
from django.conf import settings
from optparse import make_option
import sys
from eve_db.ccp_importer import util
from eve_db.ccp_importer import importers

def exit_with_error(error_msg):
    """
    Gracefully kills the script when an error was occured.
    """
    print error_msg
    sys.exit(1)
    
def exit_with_succ():
    """
    Nothing to see here, move along.
    """
    sys.exit(0)
    
def list_tables(option, opt, value, parser):
    """
    Prints a list of tables that are available for import.
    """
    print "CCP Data Dump Table List"
    print "------------------------"
    for table in util.IMPORT_LIST:
        print "%s" % table.__name__.replace('Importer_', '')
    print "-- %d tables --" % len(util.IMPORT_LIST)
    # The -l argument is just used for listing, proceed no further.
    exit_with_succ()
    
def check_for_eve_db():
    """
    Checks for the presence of the CCP EVE dump in SQLite format. Exit if
    this can't be found.
    """
    try:
        dbfile = open(settings.EVE_CCP_DUMP_SQLITE_DB, 'r')
    except IOError:
        exit_with_error("""No CCP data dump could be found. Visit 
http://wiki.eve-id.net/CCP_Database_Dump_Resources#Conversions
and download the latest SQLite conversion. Copy the SQLite .db file to the 
same directory as your settings.py file and re-name it to ccp_dump.db. You 
should then be able to run this command without issue.""")
    
def get_importer_classes_from_arg_list(arg_list):
    """
    Validates the user input for tables to import against the importer list.
    Returns a list of importer classes. In the event that one of the
    arguments does not match up against an importer class, raise an
    exception so the user may be notified.
    """
    importer_classes = set()
    for arg in arg_list:
        importer_class = getattr(importers, 'Importer_%s' % arg, False)
        if importer_class not in util.IMPORT_LIST:
            exit_with_error("No such table to import: %s" % arg)
        else:
            importer_classes.add(importer_class)
    return importer_classes

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--noinput', action='store_false', dest='interactive', default=True,
            help='Tells Django to NOT prompt the user for input of any kind.'),
        make_option("-i", "--include-deps", action="store_true",
                          dest="include_deps", default=False,
                          help="""Import the other tables that the specified table 
                                  [recursively] depends on."""),
        make_option("-l", "--list", action="callback",
                          callback=list_tables,
                          help="List all of the tables in the CCP dump and exit."),
    )
    help = """This importer script will either import one or all tables from
the CCP data dump. If no arguments are specified, all tables will be imported."""
    args = '[table_name1] [table_name2] [...]'

    requires_model_validation = False
            
    def handle(self, *args, **options):
        """
        This is where the user input is handled, and the appropriate
        actions are taken.
        """
        #print "OPTIONS", options
        #print "ARGS:", args
        check_for_eve_db()
        
        try:
            if len(args) == 0:
                print "No table names specified, importing all."
                util.run_importers(util.IMPORT_LIST)
            else:
                print "Importing: %s" % args
                importers = get_importer_classes_from_arg_list(args)
                
                include_deps = options.get('include_deps')
                if include_deps:
                    print "Calculating dependencies."

                util.run_importers(importers, include_deps=include_deps)
        except KeyboardInterrupt:
            print "Terminating early..."
            exit_with_succ()
