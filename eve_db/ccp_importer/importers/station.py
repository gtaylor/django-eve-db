"""
Import station related data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_ramActivities(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from ramActivities'):
            imp_obj, created = EVEResearchAndMfgActivity.objects.get_or_create(id=row['activityID'])
            imp_obj.name = row['activityName']
            imp_obj.description = row['description']
            
            if row['iconNo']:
                imp_obj.icon_filename = row['iconNo']
            
            if row['published'] == 1:
                imp_obj.is_published = True
            else:
                imp_obj.is_published = False
    
            imp_obj.save()
        c.close()

class Importer_staServices(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from staServices'):
            imp_obj, created = EVEStationService.objects.get_or_create(id=row['serviceID'])
            imp_obj.name = row['serviceName']
            imp_obj.description = row['description']
            imp_obj.save()
        c.close()