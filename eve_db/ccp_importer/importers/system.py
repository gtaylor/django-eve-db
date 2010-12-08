#!/usr/bin/env python
"""
Import various important system tables.
"""
from eve_db.models import EveUnit, EveName, EveGraphic, EveIcon
from importer_classes import SQLImporter, parse_int_bool



class Importer_eveUnits(SQLImporter):
    model = EveUnit
    pks = (('id', 'unitid'),)
    field_map = (('name', 'unitname'),
                 ('display_name', 'displayname'),
                 ('description', 'description'))


class Importer_eveNames(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invCategories', 'invGroups']
    model = EveName
    pks = (('id', 'itemID'),)
    field_map = (('name', 'itemName'),
                 ('category_id', 'categoryID'),
                 ('group_id', 'groupID'),
                 ('type_id', 'typeID'))

#    def import_row(self, row):
#        new_instance = self.model(id=row['itemID'],
#                                  name=row['itemName'],
#                                  category_id=row['categoryID'],
#                                  group_id=row['groupID'],
#                                  type_id=row['typeID'])
#        if self.insert_only:
#            return new_instance, True
#
#        try:
#            old_instance = self.model.objects.get(id=row['itemID'])
#            old_instance.name = row['itemName']
#            old_instance.category_id = row['categoryID']
#            old_instance.group_id = row['groupID']
#            old_instance.type_id = row['typeID']
#            return old_instance, False
#        except self.model.DoesNotExist:
#            return new_instance, True


class Importer_eveIcons(SQLImporter):
    model = EveIcon
    pks = (('id', 'iconID'),)
    field_map = (('file', 'iconFile'),
                 ('description', 'description'),)


class Importer_eveGraphics(SQLImporter):
    model = EveGraphic
    pks = (('id', 'graphicID'),)
    field_map = (('name', 'graphicName'),
                 ('file', 'graphicFile'),
                 ('description', 'description'),
                 ('is_obsolete', 'obsolete', parse_int_bool))
