"""
Import station related data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_ramActivities(SQLImporter):
    def import_row(self, row):
        imp_obj, created = EVERamActivity.objects.get_or_create(id=row['activityID'])
        imp_obj.name = row['activityName']
        imp_obj.description = row['description']
        
        if row['iconNo']:
            imp_obj.icon_filename = row['iconNo']
        
        if row['published'] == 1:
            imp_obj.is_published = True
        else:
            imp_obj.is_published = False

        imp_obj.save()
        
class Importer_ramAssemblyLineTypes(SQLImporter):
    DEPENDENCIES = ['ramActivities']
    def import_row(self, row):
        imp_obj, created = EVERamAssemblyLineType.objects.get_or_create(id=row['assemblyLineTypeID'])
        imp_obj.name = row['assemblyLineTypeName']
        imp_obj.description = row['description']
        imp_obj.base_time_multiplier = row['baseTimeMultiplier']
        imp_obj.base_material_multiplier = row['baseMaterialMultiplier']
        imp_obj.volume = row['volume']
        imp_obj.activity = EVERamActivity.objects.get(id=row['activityID'])
        imp_obj.min_cost_per_hour = row['minCostPerHour']
        imp_obj.save()

class Importer_staServices(SQLImporter):
    def import_row(self, row):
        imp_obj, created = EVEStationService.objects.get_or_create(id=row['serviceID'])
        imp_obj.name = row['serviceName']
        imp_obj.description = row['description']
        imp_obj.save()

class Importer_staStationTypes(SQLImporter):
    DEPENDENCIES = ['eveGraphics', 'staOperations', 'invTypes']
    
    def import_row(self, row):
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
        
class Importer_staOperations(SQLImporter):
    DEPENDENCIES = ['staStationTypes']
    
    def import_row(self, row):
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
        
class Importer_staStations(SQLImporter):
    DEPENDENCIES = ['invTypes', 'staOperations', 'staStationTypes',
                    'chrNPCCorporations', 'mapSolarSystems', 
                    'mapConstellations', 'mapRegions']

    def import_row(self, row):
        station, created = EVEStation.objects.get_or_create(id=row['stationID'])
        station.security = row['security']
        station.docking_cost_per_volume = row['dockingCostPerVolume']
        station.max_ship_volume_dockable = row['maxShipVolumeDockable']
        station.office_rental_cost = row['officeRentalCost']
        station.name = row['stationName']
        station.x = row['x']
        station.y = row['y']
        station.z = row['z']
        station.reprocessing_efficiency = row['reprocessingEfficiency']
        station.reprocessing_stations_take = row['reprocessingStationsTake']
        station.reprocessing_hangar_flag = row['reprocessingHangarFlag']
        
        if row['operationID']:
            station.operation, created = EVEStationOperation.objects.get_or_create(id=row['operationID'])
        
        if row['stationTypeID']:
            invtype, created = EVEInventoryType.objects.get_or_create(id=row['stationTypeID'])
            station.type, created = EVEStationType.objects.get_or_create(type=invtype)
            
        if row['corporationID']:
            station.corporation, created = EVENPCCorporation.objects.get_or_create(id=row['corporationID'])
            
        if row['solarSystemID']:
            station.solar_system = EVESolarSystem.objects.get(id=row['solarSystemID'])
            
        if row['constellationID']:
            station.constellation = EVEConstellation.objects.get(id=row['constellationID'])
            
        if row['regionID']:
            station.region = EVERegion.objects.get(id=row['regionID'])
            
        station.save()