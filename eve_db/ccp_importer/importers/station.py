"""
Import station related data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_ramActivities(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from ramActivities'):
            imp_obj, created = EVEResearchAndMfgActivity.objects.get_or_create(id=row['activityID'])
            imp_obj.name = row['activityName']
            imp_obj.description = row['description']
            
            if row['iconNo']:
                imp_obj.icon_filename = row['iconNo']
            
            if row['published'] == 1:
                imp_obj.is_published = True
            else:
                imp_obj.is_published = False
    
            imp_obj.save()
        c.close()

class Importer_staServices(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from staServices'):
            imp_obj, created = EVEStationService.objects.get_or_create(id=row['serviceID'])
            imp_obj.name = row['serviceName']
            imp_obj.description = row['description']
            imp_obj.save()
        c.close()

class Importer_staStationTypes(SQLImporter):
    DEPENDENCIES = ['eveGraphics', 'staOperations', 'invTypes']
    
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from staStationTypes'):
            invtype, created = EVEInventoryType.objects.get_or_create(id=row['stationTypeID'])
            statype, created = EVEStationType.objects.get_or_create(type=invtype)
            statype.type = invtype
            statype.dock_entry_x = row['dockEntryX']
            statype.dock_orientation_x = row['dockOrientationX']
            statype.dock_entry_y = row['dockEntryY']
            statype.dock_orientation_y = row['dockOrientationY']
            statype.dock_entry_z = row['dockEntryZ']
            statype.dock_orientation_z = row['dockOrientationZ']
            statype.office_slots = row['officeSlots']
            statype.reprocessing_efficiency = row['reprocessingEfficiency']
                
            if row['dockingBayGraphicID']:
                statype.docking_bay_graphic = EVEGraphic.objects.get(id=row['dockingBayGraphicID'])
                
            if row['hangarGraphicID']:
                statype.hangar_graphic = EVEGraphic.objects.get(id=row['hangarGraphicID'])
                
            if row['operationID']:
                statype.operation, created = EVEStationOperation.objects.get_or_create(id=row['operationID'])
            
            if row['conquerable'] == 1:
                statype.is_conquerable = True
                
            statype.save()
        c.close()
        
class Importer_staOperations(SQLImporter):
    DEPENDENCIES = ['staStationTypes']
    
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from staOperations'):
            operation, created = EVEStationOperation.objects.get_or_create(id=row['operationID'])
            operation.activity_id = row['activityID']
            operation.name = row['operationName']
            operation.description = row['description']
            operation.fringe = row['fringe']
            operation.corridor = row['corridor']
            operation.hub = row['hub']
            operation.border = row['border']
            operation.ratio = row['ratio']        
            
            if row['caldariStationTypeID']:
                invtype, created = EVEInventoryType.objects.get_or_create(id=row['caldariStationTypeID'])
                operation.caldari_station_type, created = EVEStationType.objects.get_or_create(type=invtype)
            
            if row['minmatarStationTypeID']:
                invtype, created = EVEInventoryType.objects.get_or_create(id=row['minmatarStationTypeID'])
                operation.minmatar_station_type, created = EVEStationType.objects.get_or_create(type=invtype)
            
            if row['amarrStationTypeID']:
                invtype, created = EVEInventoryType.objects.get_or_create(id=row['amarrStationTypeID'])
                operation.amarr_station_type, created = EVEStationType.objects.get_or_create(type=invtype)
            
            if row['gallenteStationTypeID']:
                invtype, created = EVEInventoryType.objects.get_or_create(id=row['gallenteStationTypeID'])
                operation.gallente_station_type, created = EVEStationType.objects.get_or_create(type=invtype)
            
            if row['joveStationTypeID']:
                invtype, created = EVEInventoryType.objects.get_or_create(id=row['joveStationTypeID'])
                operation.jove_station_type, created = EVEStationType.objects.get_or_create(type=invtype)
            
            operation.save()
        c.close()  