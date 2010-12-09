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
    model = RamAssemblyLineTypeDetailPerCategory
    pks = (('assembly_line_type', 'assemblyLineTypeID'),
           ('category', 'categoryID'))
    field_map = (('time_multiplier', 'timeMultiplier'),
                 ('material_multiplier', 'materialMultiplier'))


class Importer_ramAssemblyLineTypeDetailPerGroup(SQLImporter):
    DEPENDENCIES = ['ramAssemblyLineTypes', 'invGroups']
    model = RamAssemblyLineTypeDetailPerGroup
    pks = (('assembly_line_type', 'assemblyLineTypeID'),
           ('group', 'groupID'))
    field_map = (('time_multiplier', 'timeMultiplier'),
                 ('material_multiplier', 'materialMultiplier'))


class Importer_staServices(SQLImporter):
    model = StaService
    pks = (('id', 'serviceID'),)
    field_map = (('name', 'serviceName'),
                 ('description', 'description'))


def get_operation(operation_id):
    if operation_id:
        return StaOperation.objects.get_or_create(id=operation_id)[0]
    return None

class Importer_staStationTypes(SQLImporter):
    DEPENDENCIES = ['eveGraphics', 'staOperations', 'invTypes']
    model = StaStationType
    pks = (('id', 'stationTypeID'),)
    field_map = (('dock_entry_x', 'dockEntryX'),
                 ('dock_orientation_x', 'dockOrientationX'),
                 ('dock_entry_y', 'dockEntryY'),
                 ('dock_orientation_y', 'dockOrientationY'),
                 ('dock_entry_z', 'dockEntryZ'),
                 ('dock_orientation_z', 'dockOrientationZ'),
                 ('office_slots', 'officeSlots'),
                 ('reprocessing_efficiency', 'reprocessingEfficiency'),
                 ('operation', 'operationID', get_operation),
                 ('is_conquerable', 'conquerable', parse_int_bool))


class Importer_staOperations(SQLImporter):
    DEPENDENCIES = ['staStationTypes']
    model = StaOperation
    pks = (('id', 'operationID'),)
    field_map = (('activity_id', 'activityID'),
                 ('name', 'operationName'),
                 ('description', 'description'),
                 ('fringe', 'fringe'),
                 ('corridor', 'corridor'),
                 ('hub', 'hub'),
                 ('border', 'border'),
                 ('ratio', 'ratio'),
                 ('caldari_station_type_id', 'caldariStationTypeID'),
                 ('minmatar_station_type_id', 'minmatarStationTypeID'),
                 ('amarr_station_type_id', 'amarrStationTypeID'),
                 ('gallente_station_type_id', 'gallenteStationTypeID'),
                 ('jove_station_type_id', 'joveStationTypeID'))


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
    model = StaStation
    pks = (('id', 'stationID'),)
    field_map = (('security', 'security'),
                 ('docking_cost_per_volume', 'dockingCostPerVolume'),
                 ('max_ship_volume_dockable', 'maxShipVolumeDockable'),
                 ('office_rental_cost', 'officeRentalCost'),
                 ('name', 'stationName'),
                 ('x', 'x'),
                 ('y', 'y'),
                 ('z', 'z'),
                 ('reprocessing_efficiency', 'reprocessingEfficiency'),
                 ('reprocessing_stations_take', 'reprocessingStationsTake'),
                 ('reprocessing_hangar_flag', 'reprocessingHangarFlag'),
                 ('operation_id', 'operationID'),
                 ('type_id', 'stationTypeID'),
                 ('corporation_id', 'corporationID'),
                 ('solar_system_id', 'solarSystemID'),
                 ('constellation_id', 'constellationID'),
                 ('region_id', 'regionID'))
