#!/usr/bin/env python
"""
Import various important system tables.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_eveUnits(SQLImporter):
    def import_row(self, row):
        imp_obj, created = EveUnit.objects.get_or_create(id=row['unitid'])
        imp_obj.name = row['unitname']
        imp_obj.display_name = row['displayname']
        imp_obj.description = row['description']
        imp_obj.save()

class Importer_eveNames(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invCategories', 'invGroups']

    def import_row(self, row):
        imp_obj = EveName(id=row['itemID'])
        imp_obj.name = row['itemName']
        imp_obj.category = InvCategory(id=row['categoryID'])
        imp_obj.group = InvGroup(id=row['groupID'])
        imp_obj.type = InvType(id=row['typeID'])
        imp_obj.save()

class Importer_eveIcons(SQLImporter):
    def import_row(self, row):
        graphic, created = EveIcon.objects.get_or_create(id=row['iconID'])
        graphic.file = row['iconFile']
        graphic.description = row['description']

        graphic.save()


class Importer_eveGraphics(SQLImporter):
    def import_row(self, row):
        graphic, created = EveGraphic.objects.get_or_create(id=row['graphicID'])
        graphic.name = row['graphicName']
        graphic.file = row['graphicFile']
        graphic.description = row['description']

        if row['obsolete'] == 1:
            graphic.is_obsolete = True

        graphic.save()
