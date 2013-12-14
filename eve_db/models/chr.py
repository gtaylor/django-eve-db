"""
Character stuff.
"""
from django.db import models

class ChrRace(models.Model):
    """
    Table lists available races. Races are numbered like bitmask - 1,2,4,8,16...

    CCP Table: chrRaces
    CCP Primary key: "raceID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    icon_id = models.IntegerField(blank=True, null=True)
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

class ChrBloodline(models.Model):
    """
    Bloodlines for newly created characters with starting attributes.

    CCP Table: chrBloodlines
    CCP Primary key: "bloodlineID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(ChrRace, blank=True, null=True,
                             related_name='bloodline_set')
    description = models.TextField(blank=True)
    male_description = models.TextField(blank=True)
    female_description = models.TextField(blank=True)
    starter_ship_type = models.ForeignKey('InvType', blank=True,
                                    null=True,
                                    related_name='bloodline_starter_ship_set')
    corporation = models.ForeignKey('CrpNPCCorporation', blank=True, null=True)
    starting_perception = models.IntegerField(default=0)
    starting_willpower = models.IntegerField(default=0)
    starting_charisma = models.IntegerField(default=0)
    starting_memory = models.IntegerField(default=0)
    starting_intelligence = models.IntegerField(default=0)
    icon_id = models.IntegerField(blank=True, null=True)
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

class ChrAncestry(models.Model):
    """
    Available Ancestries with bonus skills and items.

    CCP Table: chrAncestries
    CCP Primary key: "ancestryID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    bloodline = models.ForeignKey(ChrBloodline, blank=True, null=True)
    description = models.TextField(blank=True)
    perception_bonus = models.IntegerField(default=0)
    willpower_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)
    memory_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    icon_id = models.IntegerField(blank=True, null=True)
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

class ChrAttribute(models.Model):
    """
    Five base Attrinutes annotated.

    CCP Table: chrAttributes
    CCP Primary key: "attributeID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    icon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Character Attribute'
        verbose_name_plural = 'Character Attributes'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class ChrFaction(models.Model):
    """
    All main Factions found in game.

    CCP Table: chrFactions
    CCP Primary key: "factionID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    solar_system = models.ForeignKey('MapSolarSystem', blank=True, null=True,
                                     related_name='faction_set')
    corporation = models.ForeignKey('CrpNPCCorporation', blank=True, null=True,
                                    related_name='faction_set')
    size_factor = models.FloatField(blank=True, null=True)
    station_count = models.IntegerField(default=0)
    station_system_count = models.IntegerField(default=0)
    icon_id = models.IntegerField(blank=True, null=True)
    races = models.IntegerField(default=0)

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
