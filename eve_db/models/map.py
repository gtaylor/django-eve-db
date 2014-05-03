"""
Map-related models.
"""
from django.db import models

class MapUniverse(models.Model):
    """
    CCP Table: mapUniverse
    CCP Primary key: "universeID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    x = models.FloatField(blank=True, null=True)
    x_min = models.FloatField(blank=True, null=True)
    x_max = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y_min = models.FloatField(blank=True, null=True)
    y_max = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    z_max = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Universe'
        verbose_name_plural = 'Universes'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class MapRegion(models.Model):
    """
    CCP Table: mapRegions
    CCP Primary key: "regionID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    faction = models.ForeignKey('ChrFaction', blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    x_min = models.FloatField(blank=True, null=True)
    x_max = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y_min = models.FloatField(blank=True, null=True)
    y_max = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    z_max = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class MapRegionJump(models.Model):
    """
    CCP Table: mapRegionJumps
    CCP Primary key: ("fromRegionID" int(11), "toRegionID" int(11))
    """
    from_region = models.ForeignKey(MapRegion,
                                    related_name='region_jumps_from_region_set')
    to_region = models.ForeignKey(MapRegion,
                                  related_name='region_jumps_to_region_set')

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Region Jump'
        verbose_name_plural = 'Region Jumps'
        unique_together = ('from_region', 'to_region')

    def __unicode__(self):
        return "%s -> %s" % (self.from_region.name,
                             self.to_region.name)

    def __str__(self):
        return self.__unicode__()

class MapConstellation(models.Model):
    """
    Represents a constellation. Note that all sovereignty data is subject
    to change, and is held in an external model. django-eve-api has a few
    of these for your convenience.

    CCP Table: mapConstellations
    CCP Primary key: "constellationID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    region = models.ForeignKey(MapRegion, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    x_min = models.FloatField(blank=True, null=True)
    x_max = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y_min = models.FloatField(blank=True, null=True)
    y_max = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    z_max = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    #alliance = models.ForeignKey('eve_api.ApiPlayerAlliance', blank=True, null=True)
    faction = models.ForeignKey('ChrFaction', blank=True, null=True)
    sovereignty_start_time = models.DateTimeField(blank=True, null=True)
    sovereignty_grace_start_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Constellation'
        verbose_name_plural = 'Constellations'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class MapConstellationJump(models.Model):
    """
    CCP Table: mapConstellationJumps
    CCP Primary key: ("fromConstellationID" int(11), "toConstellationID" int(11))
    """
    from_region = models.ForeignKey(MapRegion,
                                    related_name='constellation_jumps_from_region_set')
    from_constellation = models.ForeignKey(MapConstellation,
                                           related_name='constellation_jumps_from_constellation_set')
    to_region = models.ForeignKey(MapRegion,
                                  related_name='constellation_jumps_to_region_set')
    to_constellation = models.ForeignKey(MapConstellation,
                                         related_name='constellation_jumps_to_constellation_set')

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Constellation Jump'
        verbose_name_plural = 'Constellation Jumps'
        unique_together = ('from_constellation', 'to_constellation')

    def __unicode__(self):
        return "%s -> %s" % (self.from_constellation.name,
                             self.to_constellation.name)

    def __str__(self):
        return self.__unicode__()

class MapSolarSystem(models.Model):
    """
    CCP Table: mapSolarSystems
    CCP Primary key: "solarSystemID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    region = models.ForeignKey(MapRegion, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    constellation = models.ForeignKey(MapConstellation, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    x_min = models.FloatField(blank=True, null=True)
    x_max = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y_min = models.FloatField(blank=True, null=True)
    y_max = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    z_max = models.FloatField(blank=True, null=True)
    luminosity = models.FloatField(blank=True, null=True)
    is_border_system = models.BooleanField(default=False)
    is_fringe_system = models.BooleanField(default=False)
    is_corridor_system = models.BooleanField(default=False)
    is_hub_system = models.BooleanField(default=False)
    is_international = models.BooleanField(default=False)
    has_interregional_link = models.BooleanField(default=False)
    has_interconstellational_link = models.BooleanField(default=False)
    security_level = models.FloatField(blank=True, null=True)
    faction = models.ForeignKey('ChrFaction', blank=True, null=True,
                                related_name='solarsystem_set')
    radius = models.FloatField(blank=True, null=True)
    sun_type = models.ForeignKey('InvType', blank=True, null=True)
    security_class = models.CharField(max_length=5, blank=True)
    #alliance = models.ForeignKey('eve_api.ApiPlayerAlliance', blank=True, null=True)
    sovereignty_level = models.IntegerField(blank=True, null=True)
    sovereignty_start_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Solar System'
        verbose_name_plural = 'Solar Systems'

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Solar System #%d" % self.id

    def __str__(self):
        return self.__unicode__()

class MapSolarSystemJump(models.Model):
    """
    CCP Table: mapSolarSystemJumps
    CCP Primary key: ("fromSolarSystemID" int(11), "toSolarSystemID" int(11))
    """
    from_region = models.ForeignKey(MapRegion, blank=True, null=True,
                                    related_name='solar_system_jumps_from_region_set')
    from_constellation = models.ForeignKey(MapConstellation, blank=True,
                                           null=True,
                                  related_name='solar_system_jumps_from_constellation_set')
    from_solar_system = models.ForeignKey(MapSolarSystem,
                                          related_name='solar_system_jumps_from_solar_system_set')
    to_region = models.ForeignKey(MapRegion, blank=True, null=True,
                                  related_name='solar_system_jumps_to_region_set')
    to_constellation = models.ForeignKey(MapConstellation, blank=True,
                                         null=True,
                                         related_name='solar_system_jumps_to_constellation_set')
    to_solar_system = models.ForeignKey(MapSolarSystem,
                                        related_name='solar_system_jumps_to_solar_system_set')

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Solar System Jump'
        verbose_name_plural = 'Solar System Jumps'
        unique_together = ('from_solar_system', 'to_solar_system')

    def __unicode__(self):
        return "%s -> %s" % (self.from_solar_system.name,
                             self.to_solar_system.name)

    def __str__(self):
        return self.__unicode__()

class MapJump(models.Model):
    """
    Jumps between stargates.

    CCP Table: mapJumps
    CCP Primary key: "stargateID" int(11)
    """
    origin_gate = models.ForeignKey('MapDenormalize',
                                    unique=True, primary_key=True,
                                    related_name='stargate_jump_origin_set')
    destination_gate = models.ForeignKey('MapDenormalize',
                                         related_name='stargate_jump_destination_set')

    class Meta:
        app_label = 'eve_db'
        ordering = ['origin_gate']
        verbose_name = 'Stargate Jump'
        verbose_name_plural = 'Stargate Jumps'

    def __unicode__(self):
        return "%s -> %s" % (self.origin_gate, self.destination_gate)

    def __str__(self):
        return self.__unicode__()

class MapCelestialStatistic(models.Model):
    """
    CCP Table: mapCelestialStatistics
    CCP Primary key: "celestialID" int(11)
    """
    celestial = models.ForeignKey('MapDenormalize', unique=True, primary_key=True)
    temperature = models.FloatField(blank=True, null=True)
    spectral_class = models.CharField(max_length=255, blank=True)
    luminosity = models.FloatField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    life = models.FloatField(blank=True, null=True)
    orbit_radius = models.FloatField(blank=True, null=True)
    eccentricity = models.FloatField(blank=True, null=True)
    mass_dust = models.FloatField(blank=True, null=True)
    mass_gas = models.FloatField(blank=True, null=True)
    is_fragmented = models.BooleanField(default=False)
    density = models.FloatField(blank=True, null=True)
    surface_gravity = models.FloatField(blank=True, null=True)
    escape_velocity = models.FloatField(blank=True, null=True)
    orbit_period = models.FloatField(blank=True, null=True)
    rotation_rate = models.FloatField(blank=True, null=True)
    is_locked = models.BooleanField(default=False)
    pressure = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['celestial']
        verbose_name = 'Celestial Statistic'
        verbose_name_plural = 'Celestial Statistics'

    def __unicode__(self):
        return "%s stats" % self.celestial.name

    def __str__(self):
        return self.__unicode__()

class MapDenormalize(models.Model):
    """
    CCP Table: mapDenormalize
    CCP Primary key: "itemID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    type = models.ForeignKey('InvType', blank=True, null=True)
    group = models.ForeignKey('InvGroup', blank=True, null=True)
    solar_system = models.ForeignKey(MapSolarSystem, blank=True, null=True)
    constellation = models.ForeignKey(MapConstellation, blank=True, null=True)
    region = models.ForeignKey(MapRegion, blank=True, null=True)
    orbit_id = models.IntegerField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    security = models.FloatField(blank=True, null=True)
    celestial_index = models.IntegerField(blank=True, null=True)
    orbit_index = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Denormalize'
        verbose_name_plural = 'Denormalizations'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class MapLandmark(models.Model):
    """
    CCP Table: mapLandmarks
    CCP Primary key: "landmarkID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    solar_system = models.ForeignKey('MapSolarSystem', blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    icon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Landmark'
        verbose_name_plural = 'Landmarks'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class MapLocationScene(models.Model):
    """
    CCP Table: MapLocationScenes
    CCP Primary key: "locationID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    graphic = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Location Scene'
        verbose_name_plural = 'Location Scenes'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class MapLocationWormholeClass(models.Model):
    """
    CCP Table: MapLocationWormholeClasses
    CCP Primary key: "locationID" smallint(6)
    """
    location = models.ForeignKey('MapDenormalize', unique=True, primary_key=True)
    wormhole_class = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['location']
        verbose_name = 'Wormhole Class'
        verbose_name_plural = 'Wormhole Classes'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class WarCombatZone(models.Model):
    """
    CCP Table: WarCombatZone
    CCP Primary key: "combatZoneID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    faction = models.ForeignKey('ChrFaction')
    center_system = models.ForeignKey('MapSolarSystem')
    description = models.TextField(blank=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Combat Zone'
        verbose_name_plural = 'Combat Zones'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class WarCombatZoneSystem(models.Model):
    """
    CCP Table: WarCombatZone
    CCP Primary key: "combatZoneID" int(11)
    """
    solar_system = models.ForeignKey('MapSolarSystem', max_length=255, blank=True)
    combat_zone = models.ForeignKey('WarCombatZone', max_length=255, blank=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Combat Zone System'
        verbose_name_plural = 'Combat Zone Systems'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()