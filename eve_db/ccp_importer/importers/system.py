#!/usr/bin/env python
"""
Import various important system tables.
"""
from eve_db.models import EveUnit
from importer_classes import SQLImporter, parse_char_notnull

class Importer_eveUnits(SQLImporter):
    model = EveUnit
    pks = (('id', 'unitid'),)
    field_map = (('name', 'unitname'),
                 ('display_name', 'displayname', parse_char_notnull),
                 ('description', 'description', parse_char_notnull))
