"""
Map-related models. 
"""
from django.db import models

class EVEUniverse(models.Model):
    """
    mapUniverse
    """
    name = models.CharField(max_length=255, blank=True)
    x = models.FloatField(blank=True, null=True)
    x_min = models.FloatField(blank=True, null=True)
    x_max = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y_min = models.FloatField(blank=True, null=True)
    y_max = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
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
    
class EVERegion(models.Model):
    """
    mapRegions
    """
    name = models.CharField(max_length=255, blank=True)
    faction = models.ForeignKey('EVEFaction', blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    x_min = models.FloatField(blank=True, null=True)
    x_max = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y_min = models.FloatField(blank=True, null=True)
    y_max = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
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
    
class EVERegionJump(models.Model):
    """
    mapRegionJumps
    """
    from_region = models.ForeignKey(EVERegion, 
                                    related_name='region_jumps_from_region_set')
    to_region = models.ForeignKey(EVERegion,
                                  related_name='region_jumps_to_region_set')
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Region Jump'
        verbose_name_plural = 'Region Jumps'
        
    def __unicode__(self):
        return "%s -> %s" % (self.from_region.name,
                             self.to_region.name)
        
    def __str__(self):
        return self.__unicode__()
        
class EVEConstellation(models.Model):
    """
    mapConstellations
    """
    name = models.CharField(max_length=255, blank=True)
    region = models.ForeignKey(EVERegion, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    x_min = models.FloatField(blank=True, null=True)
    x_max = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y_min = models.FloatField(blank=True, null=True)
    y_max = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    alliance = models.ForeignKey('eve_api.EVEPlayerAlliance', blank=True, null=True)
    faction = models.ForeignKey('EVEFaction', blank=True, null=True)
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
    
class EVEConstellationJump(models.Model):
    """
    mapConstellationJumps
    """
    from_region = models.ForeignKey(EVERegion, 
                                    related_name='constellation_jumps_from_region_set')
    from_constellation = models.ForeignKey(EVEConstellation,
                                           related_name='constellation_jumps_from_constellation_set')
    to_region = models.ForeignKey(EVERegion,
                                  related_name='constellation_jumps_to_region_set')
    to_constellation = models.ForeignKey(EVEConstellation,
                                         related_name='constellation_jumps_to_constellation_set')
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Constellation Jump'
        verbose_name_plural = 'Constellation Jumps'
        
    def __unicode__(self):
        return "%s -> %s" % (self.from_constellation.name,
                             self.to_constellation.name)
        
    def __str__(self):
        return self.__unicode__()
    
class EVESolarSystem(models.Model):
    """
    mapSolarSystems
    """
    region = models.ForeignKey(EVERegion, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    constellation = models.ForeignKey(EVEConstellation, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    x_min = models.FloatField(blank=True, null=True)
    x_max = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y_min = models.FloatField(blank=True, null=True)
    y_max = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    z_min = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    luminosity = models.FloatField(blank=True, null=True)
    is_border_system = models.BooleanField(default=False)
    is_fringe_system = models.BooleanField(default=False)
    is_corridor_system = models.BooleanField(default=False)
    is_hub_system = models.BooleanField(default=False)
    is_international = models.BooleanField(default=False)
    has_interregional_link = models.BooleanField(default=False)
    has_interconstellational_link = models.BooleanField(default=False)
    security_level = models.FloatField(blank=True, null=True)
    faction = models.ForeignKey('EVEFaction', blank=True, null=True,
                                related_name='solarsystem_set')
    radius = models.FloatField(blank=True, null=True)
    sun_type = models.ForeignKey('EVEInventoryType', blank=True, null=True)
    security_class = models.CharField(max_length=5, blank=True)
    alliance = models.ForeignKey('eve_api.EVEPlayerAlliance', blank=True, null=True)
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
    
class EVESolarSystemJump(models.Model):
    """
    mapSolarSystemJumps
    """
    from_region = models.ForeignKey(EVERegion, blank=True, null=True,
                                    related_name='solar_system_jumps_from_region_set')
    from_constellation = models.ForeignKey(EVEConstellation, blank=True, 
                                           null=True,
                                  related_name='solar_system_jumps_from_constellation_set')
    from_solar_system = models.ForeignKey(EVESolarSystem,
                                          related_name='solar_system_jumps_from_solar_system_set')
    to_region = models.ForeignKey(EVERegion, blank=True, null=True,
                                  related_name='solar_system_jumps_to_region_set')
    to_constellation = models.ForeignKey(EVEConstellation, blank=True, 
                                         null=True,
                                         related_name='solar_system_jumps_to_constellation_set')
    to_solar_system = models.ForeignKey(EVESolarSystem,
                                        related_name='solar_system_jumps_to_solar_system_set')
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Solar System Jump'
        verbose_name_plural = 'Solar System Jumps'
        
    def __unicode__(self):
        return "%s -> %s" % (self.from_solar_system.name,
                             self.to_solar_system.name)
        
    def __str__(self):
        return self.__unicode__()
    
class EVEStargateJump(models.Model):
    """
    mapJumps
    """
    origin_gate = models.ForeignKey('EVEMapDenormalize',
                                    related_name='stargate_jump_origin_set')
    destination_gate = models.ForeignKey('EVEMapDenormalize',
                                         related_name='stargate_jump_destination_set')
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Stargate Jump'
        verbose_name_plural = 'Stargate Jumps'
        
    def __unicode__(self):
        return "%s -> %s" % (self.origin_gate, self.destination_gate)
        
    def __str__(self):
        return self.__unicode__()
    
class EVECelestialStatistic(models.Model):
    """
    mapCelestialStatistics
    """
    celestial = models.ForeignKey('EVEMapDenormalize')
    temperature = models.FloatField(blank=True, null=True)
    spectral_class = models.CharField(max_length=255, blank=True)
    luminousity = models.FloatField(blank=True, null=True)
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
        ordering = ['id']
        verbose_name = 'Celestial Statistic'
        verbose_name_plural = 'Celestial Statistics'
        
    def __unicode__(self):
        return "%s stats" % self.celestial.name
        
    def __str__(self):
        return self.__unicode__()
        
class EVEMapDenormalize(models.Model):
    """
    mapDenormalize
    """
    type = models.ForeignKey('EVEInventoryType', blank=True, null=True)
    group = models.ForeignKey('EVEInventoryGroup', blank=True, null=True)
    solar_system = models.ForeignKey(EVESolarSystem, blank=True, null=True)
    constellation = models.ForeignKey(EVEConstellation, blank=True, null=True)
    region = models.ForeignKey(EVERegion, blank=True, null=True)
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
    
class EVELandmark(models.Model):
    """
    mapLandmarks
    """
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    solar_system = models.ForeignKey('EVESolarSystem', blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    importance = models.IntegerField(blank=True, null=True)
    url_2d = models.CharField(max_length=255, blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Landmark'
        verbose_name_plural = 'Landmarks'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()