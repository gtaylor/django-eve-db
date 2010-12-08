"""
Import map data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

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

    def import_row(self, row):
        imp_obj, created = MapSolarSystem.objects.get_or_create(id=row['solarSystemID'])
        imp_obj.name = row['solarSystemName']
        imp_obj.x = row['x']
        imp_obj.x_min = row['xMin']
        imp_obj.x_max = row['xMax']
        imp_obj.y = row['y']
        imp_obj.y_min = row['yMin']
        imp_obj.y_max = row['yMax']
        imp_obj.z = row['z']
        imp_obj.z_min = row['zMin']
        imp_obj.z_max = row['zMax']
        imp_obj.radius = row['radius']
        imp_obj.luminosity = row['luminosity']
        imp_obj.security_level = row['security']

        if row['securityClass']:
            imp_obj.security_class = row['securityClass']

        if row['border'] == 1:
            imp_obj.is_border_system = True

        if row['fringe'] == 1:
            imp_obj.is_fringe_system = True

        if row['corridor'] == 1:
            imp_obj.is_corridor_system = True

        if row['hub'] == 1:
            imp_obj.is_hub_system = True

        if row['international'] == 1:
            imp_obj.is_international = True

        if row['regional'] == 1:
            imp_obj.has_interregional_link = True

        if row['constellation'] == 1:
            imp_obj.has_interconstellational_link = True

        if row['regionID']:
            imp_obj.region_id = row['regionID']

        if row['constellationID']:
            imp_obj.constellation_id = row['constellationID']

        if row['sunTypeID']:
            imp_obj.sun_type_id = row['sunTypeID']

        if row['factionID']:
            imp_obj.faction_id = row['factionID']

        imp_obj.save()

class Importer_mapSolarSystemJumps(SQLImporter):
    DEPENDENCIES = ['mapRegions', 'mapConstellations', 'mapSolarSystems']

    def import_row(self, row):
        from_constellation = MapConstellation(id=row['fromConstellationID'])
        from_region = MapRegion(id=row['fromRegionID'])
        to_constellation = MapConstellation(id=row['toConstellationID'])
        to_region = MapRegion(id=row['toRegionID'])
        from_solar_system = MapSolarSystem(id=row['fromSolarSystemID'])
        to_solar_system = MapSolarSystem(id=row['toSolarSystemID'])
        imp_obj, created = MapSolarSystemJump.objects.get_or_create(from_constellation=from_constellation,
                                                                    from_region=from_region,
                                                                    to_constellation=to_constellation,
                                                                    to_region=to_region,
                                                                    from_solar_system=from_solar_system,
                                                                    to_solar_system=to_solar_system)

    def import_new_row(self, row):
        imp_obj = MapSolarSystemJump(from_constellation_id=row['fromConstellationID'],
                                    from_region_id=row['fromRegionID'],
                                    to_constellation_id=row['toConstellationID'],
                                    to_region_id=row['toRegionID'],
                                    from_solar_system_id=row['fromSolarSystemID'],
                                    to_solar_system_id=row['toSolarSystemID'])
        imp_obj.save()

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

    def import_row(self, row):
        mapdenorm = MapDenormalize(id=row['itemID'])
        mapdenorm.orbit_id = row['orbitID']
        mapdenorm.x = row['x']
        mapdenorm.y = row['y']
        mapdenorm.z = row['z']
        mapdenorm.radius = row['radius']
        mapdenorm.name = row['itemName']
        mapdenorm.security = row['security']
        mapdenorm.celestial_index = row['celestialIndex']
        mapdenorm.orbit_index = row['orbitIndex']

        if row['typeID']:
            mapdenorm.type_id = row['typeID']

        if row['groupID']:
            mapdenorm.group_id = row['groupID']

        if row['solarSystemID']:
            mapdenorm.solar_system_id = row['solarSystemID']

        if row['constellationID']:
            mapdenorm.constellation_id = row['constellationID']

        if row['regionID']:
            mapdenorm.region_id = row['regionID']

        return mapdenorm

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
