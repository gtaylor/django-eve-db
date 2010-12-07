#!/usr/bin/env python
"""
Import various important system tables.
"""
from eve_db.models import EveUnit, EveName, EveGraphic, EveIcon
from importer_classes import SQLImporter

class Importer_eveUnits(SQLImporter):
    model = EveUnit
    
    def import_row(self, row):
        new_instance = self.model(id=row['unitid'],
                                  name=row['unitname'],
                                  display_name=row['displayname'],
                                  description=row['description'])
        if self.insert_only:
            return new_instance, True
        
        try:
            old_instance = self.model.objects.get(id=row['unitid'])
            old_instance.name = row['unitname']
            old_instance.display_name = row['displayname']
            old_instance.description = row['description']
            return old_instance, False
        except self.model.DoesNotExist:
            return new_instance, True

class Importer_eveNames(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invCategories', 'invGroups']
    model = EveName

    def import_row(self, row):
        new_instance = self.model(id=row['itemID'],
                                  name=row['itemName'],
                                  category_id=row['categoryID'],
                                  group_id=row['groupID'],
                                  type_id=row['typeID'])
        if self.insert_only:
            return new_instance, True
        
        try:
            old_instance = self.model.objects.get(id=row['itemID'])
            old_instance.name = row['itemName']
            old_instance.category_id = row['categoryID']
            old_instance.group_id = row['groupID']
            old_instance.type_id = row['typeID']
            return old_instance, False
        except self.model.DoesNotExist:
            return new_instance, True

class Importer_eveIcons(SQLImporter):
    model = EveIcon
    pks = (('id', 'iconID'),)
    field_map = (('file', 'iconFile'),
                 ('description', 'description'),) 


class Importer_eveGraphics(SQLImporter):
    model = EveGraphic
    
    def import_row(self, row):
        new_instance = self.model(id=row['graphicID'],
                                  name=row['graphicName'],
                                  file=row['graphicFile'],
                                  description=row['description'],
                                  is_obsolete=True if row['obsolete'] == 1 else False)
        if self.insert_only:
            return new_instance, True
        
        try:
            old_instance = self.model.objects.get(id=row['graphicID'])
            old_instance.name = row['graphicName']
            old_instance.file = row['graphicFile']
            old_instance.description = row['description']
            old_instance.is_obsolete = True if row['obsolete'] == 1 else False
            return old_instance, False
        except self.model.DoesNotExist:
            return new_instance, True
