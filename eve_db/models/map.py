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