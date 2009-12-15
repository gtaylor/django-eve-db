"""
Map-related models. 
"""
from django.db import models

class Universe(models.Model):
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
    
class Region(models.Model):
    """
    mapRegions
    """
    name = models.CharField(max_length=255, blank=True)
    faction = models.ForeignKey('Faction', blank=True, null=True)
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
    
class Constellation(models.Model):
    """
    mapConstellations
    """
    name = models.CharField(max_length=255, blank=True)
    region = models.ForeignKey(Region, blank=True, null=True)
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
    alliance = models.ForeignKey('EVEPlayerAlliance', blank=True, null=True)
    faction = models.ForeignKey('Faction', blank=True, null=True)
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
    
class SolarSystem(models.Model):
    """
    mapSolarSystems
    """
    region = models.ForeignKey(Region, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    constellation = models.ForeignKey(Constellation, blank=True, null=True)
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
    faction = models.ForeignKey('Faction', blank=True, null=True,
                                related_name='solarsystem_set')
    radius = models.FloatField(blank=True, null=True)
    sun_type = models.ForeignKey('EVEInventoryType', blank=True, null=True)
    security_class = models.CharField(max_length=5, blank=True)
    alliance = models.ForeignKey('EVEPlayerAlliance', blank=True, null=True)
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