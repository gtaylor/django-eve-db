"""
Import map data.
"""
from eve_db.models import map as map_models
from importer_classes import SQLImporter, parse_int_bool, parse_char_notnull



class Importer_mapUniverse(SQLImporter):
    model = map_models.MapUniverse
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
    model = map_models.MapRegion
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
    model = map_models.MapRegionJump
    pks = (('from_region', 'fromRegionID'), ('to_region', 'toRegionID'))


class Importer_mapConstellations(SQLImporter):
    DEPENDENCIES = ['chrFactions', 'mapRegions']
    model = map_models.MapConstellation
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
    model = map_models.MapConstellationJump
    pks = (('from_constellation', 'fromConstellationID'),
           ('to_constellation', 'toConstellationID'))
    field_map = (('from_region_id', 'fromRegionID'),
                 ('to_region_id', 'toRegionID'))


class Importer_mapSolarSystems(SQLImporter):
    DEPENDENCIES = ['chrFactions', 'mapRegions', 'mapConstellations',
                    'invTypes']
    model = map_models.MapSolarSystem
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
    model = map_models.MapSolarSystemJump
    pks = (('from_solar_system', 'fromSolarSystemID'),
           ('to_solar_system', 'toSolarSystemID'))
    field_map = (('from_region_id', 'fromRegionID'),
                 ('to_region_id', 'toRegionID'),
                 ('from_constellation_id', 'fromConstellationID'),
                 ('to_constellation_id', 'toConstellationID'))


class Importer_mapJumps(SQLImporter):
    DEPENDENCIES = ['mapDenormalize']
    model = map_models.MapJump
    pks = (('origin_gate', 'stargateID'),)
    field_map = (('destination_gate_id', 'celestialID'),)


class Importer_mapDenormalize(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invGroups', 'mapSolarSystems',
                    'mapConstellations', 'mapRegions']
    model = map_models.MapDenormalize
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
    DEPENDENCIES = ['mapSolarSystems']
    model = map_models.MapLandmark
    pks = (('id', 'landmarkID'),)
    field_map = (('name', 'landmarkName'),
                 ('x', 'x'),
                 ('y', 'y'),
                 ('z', 'z'),
                 ('solar_system_id', 'locationID'),
                 ('icon_id', 'iconID'))


class Importer_mapCelestialStatistics(SQLImporter):
    DEPENDENCIES = ['mapDenormalize']
    model = map_models.MapCelestialStatistic
    pks = (('celestial', 'celestialID'),)
    field_map = (('temperature', 'temperature'),
                 ('spectral_class', 'spectralClass'),
                 ('luminosity', 'luminosity'),
                 ('age', 'age'),
                 ('life', 'life'),
                 ('orbit_radius', 'orbitRadius'),
                 ('eccentricity', 'eccentricity'),
                 ('mass_dust', 'massDust'),
                 ('mass_gas', 'massGas'),
                 ('density', 'density'),
                 ('surface_gravity', 'surfaceGravity'),
                 ('escape_velocity', 'escapeVelocity'),
                 ('orbit_period', 'orbitPeriod'),
                 ('rotation_rate', 'rotationRate'),
                 ('pressure', 'pressure'),
                 ('radius', 'radius'),
                 ('mass', 'mass'),
                 ('is_locked', 'locked', parse_int_bool),
                 ('is_fragmented', 'fragmented', parse_int_bool))

class Importer_mapLocationScenes(SQLImporter):
    model = map_models.MapLocationScene
    pks = (('id', 'locationID'),)
    field_map = (('graphic', 'graphicID'),)

class Importer_mapLocationWormholeClasses(SQLImporter):
    DEPENDENCIES = ['mapDenormalize']
    model = map_models.MapLocationWormholeClass
    pks = (('location_id', 'locationID'),)
    field_map = (('wormhole_class', 'wormholeClassID'),)

class Importer_warCombatZones(SQLImporter):
    DEPENDENCIES = ['chrFactions', 'mapSolarSystems']
    model = map_models.WarCombatZone
    pks = (('id', 'combatZoneID'),)
    field_map = (('name', 'combatZoneName'),
                ('faction_id', 'factionID'),
                ('center_system_id', 'centerSystemID'),
                ('description', 'description'))

class Importer_warCombatZoneSystems(SQLImporter):
    DEPENDENCIES = ['warCombatZones', 'mapSolarSystems']
    model = map_models.WarCombatZoneSystem
    pks = (('solar_system', 'solarSystemID'),)
    field_map = (('combat_zone_id', 'combatZoneID'),)