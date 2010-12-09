"""
Import planetary interaction related data.
"""
from eve_db.models import PlanetSchematic, PlanetSchematicsPinMap, PlanetSchematicsTypeMap
from importer_classes import SQLImporter, parse_int_bool



class Importer_planetSchematics(SQLImporter):
    model = PlanetSchematic
    pks = (('id', 'schematicID'),)
    field_map = (('name', 'schematicName'),
                 ('cycle_time', 'cycleTime'))


class Importer_planetSchematicsPinMap(SQLImporter):
    DEPENDENCIES = ['invTypes', 'planetSchematics']
    model = PlanetSchematicsPinMap
    pks = (('type', 'pinTypeID'), ('schematic', 'schematicID'))


class Importer_planetSchematicsTypeMap(SQLImporter):
    DEPENDENCIES = ['invTypes', 'planetSchematics']
    model = PlanetSchematicsTypeMap
    pks = (('type', 'typeID'), ('schematic', 'schematicID'))
    field_map = (('quantity', 'quantity'),
                 ('is_input', 'isInput', parse_int_bool))
