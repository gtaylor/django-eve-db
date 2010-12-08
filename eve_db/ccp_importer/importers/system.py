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
