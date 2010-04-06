#!/usr/bin/env python
"""
Import various important system tables.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_eveUnits(SQLImporter):
    def import_row(self, row):
        imp_obj, created = EVEUnit.objects.get_or_create(id=row['unitid'])
        imp_obj.name = row['unitname']
        imp_obj.display_name = row['displayname']
        imp_obj.description = row['description']
        imp_obj.save()
        
class Importer_eveNames(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invCategories', 'invGroups']

    def import_row(self, row):
        imp_obj, created = EveName.objects.get_or_create(id=row['itemID'])
        imp_obj.name = row['itemName']
        imp_obj.category = InvCategory.objects.get(id=row['categoryID'])
        imp_obj.group = InvGroup.objects.get(id=row['groupID'])
        imp_obj.type = InvType.objects.get(id=row['typeID'])
        imp_obj.save()

class Importer_eveGraphics(SQLImporter):
    def import_row(self, row):
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