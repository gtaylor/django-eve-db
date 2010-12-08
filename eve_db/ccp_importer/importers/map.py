"""
Import map data.
"""
from eve_db.models import *
from importer_classes import SQLImporter, parse_int_bool, parse_char_notnull

class Importer_mapUniverse(SQLImporter):
    model = MapUniverse
    pks = (('id', 'universeID'),)
    field_map = (('name', 'universeName'),
                 ('x', 'x'),
                 ('x_min', 'xMin'),
                 ('x_max', 'xMax'),
                 ('y', 'y'),
                 ('y_min', 'yMin'),
                 ('y_max', 'yMax'),
                 ('z', 'z'),
                 ('z_min', 'zMin'),
                 ('z_max', 'zMax'),
                 ('radius', 'radius'))


class Importer_mapRegions(SQLImporter):
    DEPENDENCIES = ['chrFactions']
    model = MapRegion
    pks = (('id', 'regionID'),)
    field_map = (('name', 'regionName'),
                 ('x', 'x'),
                 ('x_min', 'xMin'),
                 ('x_max', 'xMax'),
                 ('y', 'y'),
                 ('y_min', 'yMin'),
                 ('y_max', 'yMax'),
                 ('z', 'z'),
                 ('z_min', 'zMin'),
                 ('z_max', 'zMax'),
                 ('faction_id', 'factionID'),
                 ('radius', 'radius'))



class Importer_mapRegionJumps(SQLImporter):
    DEPENDENCIES = ['mapRegions']
    model = MapRegionJump
    pks = (('from_region', 'fromRegionID'), ('to_region', 'toRegionID'))


class Importer_mapConstellations(SQLImporter):
    DEPENDENCIES = ['chrFactions', 'mapRegions']
    model = MapConstellation
    pks = (('id', 'constellationID'),)
    field_map = (('name', 'constellationName'),
                 ('x', 'x'),
                 ('x_min', 'xMin'),
                 ('x_max', 'xMax'),
                 ('y', 'y'),
                 ('y_min', 'yMin'),
                 ('y_max', 'yMax'),
                 ('z', 'z'),
                 ('z_min', 'zMin'),
                 ('z_max', 'zMax'),
                 ('region_id', 'regionID'),
                 ('faction_id', 'factionID'),
                 ('radius', 'radius'))


class Importer_mapConstellationJumps(SQLImporter):
    DEPENDENCIES = ['mapRegions', 'mapConstellations']
    model = MapConstellationJump
    pks = (('from_constellation', 'fromConstellationID'),
           ('to_constellation', 'toConstellationID'))
    field_map = (('from_region_id', 'fromRegionID'),
                 ('to_region_id', 'toRegionID'))


class Importer_mapSolarSystems(SQLImporter):
    DEPENDENCIES = ['chrFactions', 'mapRegions', 'mapConstellations',
                    'invTypes']
    model = MapSolarSystem
    pks = (('id', 'solarSystemID'),)
    field_map = (('name', 'solarSystemName'),
                 ('x', 'x'),
                 ('x_min', 'xMin'),
                 ('x_max', 'xMax'),
                 ('y', 'y'),
                 ('y_min', 'yMin'),
                 ('y_max', 'yMax'),
                 ('z', 'z'),
                 ('z_min', 'zMin'),
                 ('z_max', 'zMax'),
                 ('radius', 'radius'),
                 ('luminosity', 'luminosity'),
                 ('security_level', 'security'),
                 ('security_class', 'securityClass', parse_char_notnull),
                 ('is_border_system', 'border', parse_int_bool),
                 ('is_fringe_system', 'fringe', parse_int_bool),
                 ('is_corridor_system', 'corridor', parse_int_bool),
                 ('is_hub_system', 'hub', parse_int_bool),
                 ('is_international', 'international', parse_int_bool),
                 ('has_interregional_link', 'regional', parse_int_bool),
                 ('has_interconstellational_link', 'constellation', parse_int_bool),
                 ('region_id', 'regionID'),
                 ('faction_id', 'factionID'),
                 ('constellation_id', 'constellationID'),
                 ('sun_type_id', 'sunTypeID'))


class Importer_mapSolarSystemJumps(SQLImporter):
    DEPENDENCIES = ['mapRegions', 'mapConstellations', 'mapSolarSystems']
    model = MapSolarSystemJump
    pks = (('from_solar_system', 'fromSolarSystemID'),
           ('to_solar_system', 'toSolarSystemID'))
    field_map = (('from_region_id', 'fromRegionID'),
                 ('to_region_id', 'toRegionID'),
                 ('from_constellation_id', 'fromConstellationID'),
                 ('to_constellation_id', 'toConstellationID'))


class Importer_mapJumps(SQLImporter):
    DEPENDENCIES = ['mapDenormalize']

    def import_row(self, row):
        origin_gate = MapDenormalize.objects.get(id=row['stargateID'])
        destination_gate = MapDenormalize.objects.get(id=row['celestialID'])
        imp_obj, created = MapJump.objects.get_or_create(origin_gate=origin_gate,
                                                                 destination_gate=destination_gate)

    def import_new_row(self, row):
        imp_obj = MapJump(origin_gate_id=row['stargateID'],
                          destination_gate_id=row['celestialID'])
        imp_obj.save()

class Importer_mapDenormalize(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invGroups', 'mapSolarSystems',
                    'mapConstellations', 'mapRegions']
    model = MapDenormalize
    pks = (('id', 'itemID'),)
    field_map = (('orbit_id', 'orbitID'),
                 ('x', 'x'),
                 ('y', 'y'),
                 ('z', 'z'),
                 ('radius', 'radius'),
                 ('name', 'itemName'),
                 ('security', 'security'),
                 ('celestial_index', 'celestialIndex'),
                 ('orbit_index', 'orbitIndex'),
                 ('type_id', 'typeID'),
                 ('group_id', 'groupID'),
                 ('solar_system_id', 'solarSystemID'),
                 ('constellation_id', 'constellationID'),
                 ('region_id', 'regionID'))


class Importer_mapLandmarks(SQLImporter):
    DEPENDENCIES = ['mapSolarSystems', 'eveIcons']

    def import_row(self, row):
        imp_obj, created = MapLandmark.objects.get_or_create(id=row['landmarkID'])
        imp_obj.name = row['landmarkName']
        imp_obj.description = row['description']
        imp_obj.x = row['x']
        imp_obj.y = row['y']
        imp_obj.z = row['z']
        imp_obj.radius = row['radius']
        imp_obj.importance = row['importance']

        if row['locationID']:
            imp_obj.solar_system = MapSolarSystem.objects.get(id=row['locationID'])

        if row['iconID']:
            imp_obj.icon = EveIcon.objects.get(id=row['iconID'])

        imp_obj.save()

class Importer_mapCelestialStatistics(SQLImporter):
    DEPENDENCIES = ['mapDenormalize']

    def import_row(self, row):
        imp_obj = MapCelestialStatistic()
        imp_obj.celestial_id = row['celestialID']
        imp_obj.temperature = row['temperature']
        imp_obj.spectral_class = row['spectralClass']
        imp_obj.luminosity = row['luminosity']
        imp_obj.age = row['age']
        imp_obj.life = row['life']
        imp_obj.orbit_radius = row['orbitRadius']
        imp_obj.eccentricity = row['eccentricity']
        imp_obj.mass_dust = row['massDust']
        imp_obj.mass_gas = row['massGas']
        imp_obj.density = row['density']
        imp_obj.surface_gravity = row['surfaceGravity']
        imp_obj.escape_velocity = row['escapeVelocity']
        imp_obj.orbit_period = row['orbitPeriod']
        imp_obj.rotation_rate = row['rotationRate']
        imp_obj.pressure = row['pressure']
        imp_obj.radius = row['radius']
        imp_obj.mass = row['mass']

        if row['locked'] == 1:
            imp_obj.is_locked = True

        if row['fragmented'] == 1:
            imp_obj.is_fragmented = True

        imp_obj.save()
