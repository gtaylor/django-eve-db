#!/usr/bin/env python
"""
Import various important system tables.
"""
from django import db
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_eveUnits(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from eveUnits'):
            imp_obj, created = EVEUnit.objects.get_or_create(id=row['unitid'])
            imp_obj.name = row['unitname']
            imp_obj.display_name = row['displayname']
            imp_obj.description = row['description']
            imp_obj.save()
            db.reset_queries()
        c.close()
        
class Importer_eveNames(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invCategories', 'invGroups']
    def run_importer(self, conn):
        c = conn.cursor()

        for row in c.execute('select * from eveNames'):
            imp_obj, created = EVEInventoryName.objects.get_or_create(id=row['itemID'])
            imp_obj.name = row['itemName']
            imp_obj.category = EVEInventoryCategory.objects.get(id=row['categoryID'])
            imp_obj.group = EVEInventoryGroup.objects.get(id=row['groupID'])
            imp_obj.type = EVEInventoryType.objects.get(id=row['typeID'])
            imp_obj.save()
            db.reset_queries()
        c.close()

class Importer_eveGraphics(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from eveGraphics'):
            graphic, created = EVEGraphic.objects.get_or_create(id=row['graphicID'])
            graphic.name = row['urlWeb']
            graphic.icon_filename = row['icon']
            graphic.description = row['description']
            
            # Handle booleans
            if row['published'] == 1:
                graphic.is_published = True
            else:
                graphic.is_published = False
                
            if row['obsolete'] == 1:
                graphic.is_obsolete = True
            else:
                graphic.is_obsolete = False
            graphic.save()
            db.reset_queries()
        c.close()