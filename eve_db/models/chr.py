"""
Character stuff. 
"""
from django.db import models

class EVERace(models.Model):
    """
    An EVE race.
    
    chrRaces
    """
    name = models.CharField(max_length=30)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    # TODO: Add allegiance to a Faction here.
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Race'
        verbose_name_plural = 'Races'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVEBloodline(models.Model):
    """
    chrBloodlines
    """
    name = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(EVERace,blank=True, null=True, 
                             related_name='bloodline_set')
    description = models.TextField(blank=True)
    male_description = models.TextField(blank=True)
    female_description = models.TextField(blank=True)
    starter_ship_type = models.ForeignKey('EVEInventoryType', blank=True,
                                    null=True,
                                    related_name='bloodline_starter_ship_set')
    corporation = models.ForeignKey('NPCCorporation', blank=True, null=True)
    starting_perception = models.IntegerField(default=0)
    starting_willpower = models.IntegerField(default=0)
    starting_charisma = models.IntegerField(default=0)
    starting_memory = models.IntegerField(default=0)
    starting_intelligence = models.IntegerField(default=0)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    short_description = models.TextField(blank=True)
    short_male_description = models.TextField(blank=True)
    short_female_description = models.TextField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Bloodline'
        verbose_name_plural = 'Bloodlines'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVEAncestry(models.Model):
    """
    chrAncestries
    """
    name = models.CharField(max_length=255, blank=True)
    bloodline = models.ForeignKey(EVEBloodline,blank=True, null=True)
    description = models.TextField(blank=True)
    perception_bonus = models.IntegerField(default=0)
    willpower_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)
    memory_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    short_description = models.TextField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Ancestry'
        verbose_name_plural = 'Ancestries'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class EVEFaction(models.Model):
    """
    chrFactions
    """
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    solar_system = models.ForeignKey('SolarSystem', blank=True, null=True,
                                     related_name='faction_set')
    corporation = models.ForeignKey('NPCCorporation', blank=True, null=True,
                                    related_name='faction_set')
    size_factor = models.FloatField(blank=True, null=True)
    station_count = models.IntegerField(default=0)
    station_system_count = models.IntegerField(default=0)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Faction'
        verbose_name_plural = 'Factions'

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Faction #%d" % self.id

    def __str__(self):
        return self.__unicode__()