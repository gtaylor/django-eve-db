#!/usr/bin/env python
"""
Import various important system tables.
"""
from eve_db.models import EveUnit, EveGraphic, EveIcon
from importer_classes import SQLImporter, parse_int_bool, parse_char_notnull

class Importer_eveUnits(SQLImporter):
    model = EveUnit
    pks = (('id', 'unitid'),)
    field_map = (('name', 'unitname'),
                 ('display_name', 'displayname', parse_char_notnull),
                 ('description', 'description', parse_char_notnull))


class Importer_eveIcons(SQLImporter):
    model = EveIcon
    pks = (('id', 'iconID'),)
    field_map = (('file', 'iconFile'),
                 ('description', 'description'),)


class Importer_eveGraphics(SQLImporter):
    model = EveGraphic
    pks = (('id', 'graphicID'),)
    field_map = (('name', 'graphicName', parse_char_notnull),
                 ('file', 'graphicFile', parse_char_notnull),
                 ('description', 'description', parse_char_notnull),
                 ('is_obsolete', 'obsolete', parse_int_bool))
