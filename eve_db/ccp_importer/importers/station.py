"""
Import station related data.
"""
from eve_db.models import *
from importer_classes import SQLImporter, parse_int_bool



class Importer_ramActivities(SQLImporter):
    model = RamActivity
    pks = (('id', 'activityID'),)
    field_map = (('name', 'activityName'),
                 ('icon_filename', 'iconNo'),
                 ('description', 'description'),
                 ('is_published', 'published', parse_int_bool))


class Importer_ramAssemblyLineTypes(SQLImporter):
    DEPENDENCIES = ['ramActivities']
    model = RamAssemblyLineType
    pks = (('id', 'assemblyLineTypeID'),)
    field_map = (('name', 'assemblyLineTypeName'),
                 ('base_time_multiplier', 'baseTimeMultiplier'),
                 ('description', 'description'),
                 ('base_material_multiplier', 'baseMaterialMultiplier'),
                 ('volume', 'volume'),
                 ('activity_id', 'activityID'),
                 ('min_cost_per_hour', 'minCostPerHour'))


class Importer_staOperationServices(SQLImporter):
    DEPENDENCIES = ['staOperations', 'staServices']

    def import_row(self, row):
        operation = StaOperation.objects.get(id=row['operationID'])
        service = StaService.objects.get(id=row['serviceID'])
        imp_obj, created = StaOperationServices.objects.get_or_create(
                                                    operation=operation,
                                                    service=service)
        imp_obj.save()

class Importer_ramAssemblyLines(SQLImporter):
    DEPENDENCIES = ['ramActivities', 'ramAssemblyLineTypes', 'staStations',
                    'crpNPCCorporations']

    def import_row(self, row):
        assembly_line_type = RamAssemblyLineType.objects.get(id=row['assemblyLineTypeID'])
        imp_obj = RamAssemblyLine(id=row['assemblyLineID'],
                                  assembly_line_type=assembly_line_type,
                                  station_id=row['containerID'],
                                  owner_id=row['ownerID'],
                                  activity_id=row['activityID'])
        imp_obj.name = assembly_line_type.name
        imp_obj.ui_grouping_id = row['UIGroupingID']
        imp_obj.cost_install = row['costInstall']
        imp_obj.cost_per_hour = row['costPerHour']
        imp_obj.discount_per_good_standing_point = row['discountPerGoodStandingPoint']
        imp_obj.surcharge_per_bad_standing_point = row['surchargePerBadStandingPoint']
        imp_obj.minimum_standing = row['minimumStanding']
        imp_obj.minimum_char_security = row['minimumCharSecurity']
        imp_obj.minimum_corp_security = row['minimumCorpSecurity']
        imp_obj.maximum_char_security = row['maximumCharSecurity']
        imp_obj.maximum_corp_security = row['maximumCorpSecurity']
        imp_obj.save

class Importer_ramAssemblyLineTypeDetailPerCategory(SQLImporter):
    DEPENDENCIES = ['ramAssemblyLineTypes', 'invCategories']

    def import_row(self, row):
        ass_type = RamAssemblyLineType.objects.get(id=row['assemblyLineTypeID'])
        category = InvCategory.objects.get(id=row['categoryID'])
        imp_obj, created = RamAssemblyLineTypeDetailPerCategory.objects.get_or_create(
                                                    assembly_line_type=ass_type,
                                                    category=category)
        imp_obj.time_multiplier = row['timeMultiplier']
        imp_obj.material_multiplier = row['materialMultiplier']
        imp_obj.save()

class Importer_ramAssemblyLineTypeDetailPerGroup(SQLImporter):
    DEPENDENCIES = ['ramAssemblyLineTypes', 'invGroups']

    def import_row(self, row):
        ass_type = RamAssemblyLineType.objects.get(id=row['assemblyLineTypeID'])
        group = InvGroup.objects.get(id=row['groupID'])
        imp_obj, created = RamAssemblyLineTypeDetailPerGroup.objects.get_or_create(
                                                    assembly_line_type=ass_type,
                                                    group=group)
        imp_obj.time_multiplier = row['timeMultiplier']
        imp_obj.material_multiplier = row['materialMultiplier']
        imp_obj.save()

class Importer_staServices(SQLImporter):
    model = StaService
    pks = (('id', 'serviceID'),)
    field_map = (('name', 'serviceName'),
                 ('description', 'description'))


class Importer_staStationTypes(SQLImporter):
    DEPENDENCIES = ['eveGraphics', 'staOperations', 'invTypes']

    def import_row(self, row):
        imp_obj, created = StaStationType.objects.get_or_create(id=row['stationTypeID'])
        imp_obj.dock_entry_x = row['dockEntryX']
        imp_obj.dock_orientation_x = row['dockOrientationX']
        imp_obj.dock_entry_y = row['dockEntryY']
        imp_obj.dock_orientation_y = row['dockOrientationY']
        imp_obj.dock_entry_z = row['dockEntryZ']
        imp_obj.dock_orientation_z = row['dockOrientationZ']
        imp_obj.office_slots = row['officeSlots']
        imp_obj.reprocessing_efficiency = row['reprocessingEfficiency']

        if row['operationID']:
            imp_obj.operation, created = StaOperation.objects.get_or_create(id=row['operationID'])

        if row['conquerable'] == 1:
            imp_obj.is_conquerable = True

        imp_obj.save()

class Importer_staOperations(SQLImporter):
    DEPENDENCIES = ['staStationTypes']

    def import_row(self, row):
        operation, created = StaOperation.objects.get_or_create(id=row['operationID'])
        operation.activity_id = row['activityID']
        operation.name = row['operationName']
        operation.description = row['description']
        operation.fringe = row['fringe']
        operation.corridor = row['corridor']
        operation.hub = row['hub']
        operation.border = row['border']
        operation.ratio = row['ratio']

        if row['caldariStationTypeID']:
            operation.caldari_station_type, created = StaStationType.objects.get_or_create(id=row['caldariStationTypeID'])

        if row['minmatarStationTypeID']:
            operation.minmatar_station_type, created = StaStationType.objects.get_or_create(id=row['minmatarStationTypeID'])

        if row['amarrStationTypeID']:
            operation.amarr_station_type, created = StaStationType.objects.get_or_create(id=row['amarrStationTypeID'])

        if row['gallenteStationTypeID']:
            operation.gallente_station_type, created = StaStationType.objects.get_or_create(id=row['gallenteStationTypeID'])

        if row['joveStationTypeID']:
            operation.jove_station_type, created = StaStationType.objects.get_or_create(id=row['joveStationTypeID'])

        operation.save()

class Importer_ramAssemblyLineStations(SQLImporter):
    DEPENDENCIES = ['staStations', 'ramAssemblyLineTypes', 'staStationTypes',
                    'chrNPCCorporations', 'mapSolarSystems',
                    'mapRegions']

    def import_row(self, row):
        imp_obj, created = RamAssemblyLineStations.objects.\
            get_or_create(station=StaStation(id=row['stationID']),
                          assembly_line_type=RamAssemblyLineType(id=row['assemblyLineTypeID']))
        imp_obj.station_type_id = row['stationTypeID']
        imp_obj.owner_id = row['ownerID']
        imp_obj.solar_system_id = row['solarSystemID']
        imp_obj.region_id = row['regionID']
        imp_obj.quantity_id = row['quantity']
        imp_obj.save()

class Importer_ramTypeRequirements(SQLImporter):
    DEPENDENCIES = ['invTypes', 'ramActivities']

    def import_row(self, row):
        imp_obj, created = RamTypeRequirement.objects.\
            get_or_create(type=InvType(id=row['typeID']),
                          activity_type=RamActivity(id=row['activityID']),
                          required_type=InvType(id=row['requiredTypeID']))
        imp_obj.quantity = row['quantity']
        imp_obj.damage_per_job = row['damagePerJob']

        if row['recycle'] == 0:
            imp_obj.recycle = False
        if row['recycle'] == 1:
            imp_obj.recycle = True

        imp_obj.save()



class Importer_staStations(SQLImporter):
    DEPENDENCIES = ['invTypes', 'staOperations', 'staStationTypes',
                    'chrNPCCorporations', 'mapSolarSystems',
                    'mapConstellations', 'mapRegions']

    def import_row(self, row):
        station = StaStation(id=row['stationID'])
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
            station.operation_id = row['operationID']

        if row['stationTypeID']:
            station.type_id = row['stationTypeID']

        if row['corporationID']:
            station.corporation_id = row['corporationID']

        if row['solarSystemID']:
            station.solar_system_id = row['solarSystemID']

        if row['constellationID']:
            station.constellation_id = row['constellationID']

        if row['regionID']:
            station.region_id = row['regionID']

        station.save()
