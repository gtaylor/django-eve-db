"""
Import planetary interaction related data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_planetSchematics(SQLImporter):
    def import_row(self, row):
        imp_obj = PlanetSchematic(id=row['schematicID'])
        imp_obj.name = row['schematicName']
        imp_obj.cycle_time = row['cycleTime']
        imp_obj.save()
    
class Importer_planetSchematicsPinMap(SQLImporter):
    DEPENDENCIES = ['invTypes', 'planetSchematics']
    
    def import_row(self, row):
        type = InvType.objects.get(id=row['pinTypeID'])
        schematic = PlanetSchematic(id=row['schematicID'])
        imp_obj, created = PlanetSchematicsPinMap.objects.get_or_create(type=type, schematic=schematic)

class Importer_planetSchematicsTypeMap(SQLImporter):
    DEPENDENCIES = ['invTypes', 'planetSchematics']
    
    def import_row(self, row):
        type = InvType.objects.get(id=row['typeID'])
        schematic = PlanetSchematic(id=row['schematicID'])
        imp_obj, created = PlanetSchematicsTypeMap.objects.get_or_create(type=type, schematic=schematic)
        imp_obj.quantity = row['quantity']
        
        if row['isInput'] == 1:
            imp_obj.is_input = True
        else:
            imp_obj.is_input = False
        
        imp_obj.save()
