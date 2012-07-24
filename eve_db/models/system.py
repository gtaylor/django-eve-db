"""
Critical components that are used throughout the other modules.
"""
from django.db import models

class EveName(models.Model):
    """
    This appears to be something used to search everything at once. Most of
    the stuff in this table have models with a 'name' field on them. The CCP
    dump doesn't use the eveNames table directly many times.
    
    Things covered by this model include space objects, corporations, and
    people.
    
    CCP Table: eveNames
    CCP Primary key: "itemID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('InvCategory', blank=True, null=True)
    group = models.ForeignKey('InvGroup', blank=True, null=True)
    type = models.ForeignKey('InvType', blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Name'
        verbose_name_plural = 'Names'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class EveUnit(models.Model):
    """
    Units of measurement.
    
    CCP Table: eveUnits
    CCP Primary key: "unitID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=75)
    display_name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class EveIcon(models.Model):
    """
    An icon.

    CCP Table: eveIcons
    CCP Primary key: "iconID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    file = models.TextField(blank=True)
    description = models.CharField(max_length=255)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Icon'
        verbose_name_plural = 'Icons'

    def __unicode__(self):
        return self.file

    def __str__(self):
        return self.__unicode__()

class EveGraphic(models.Model):
    """
    Stored graphic model.

    CCP Table: eveGraphics
    CCP Primary key: "graphicID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    file = models.TextField(blank=True)
    is_obsolete = models.BooleanField(default=False)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Graphic'
        verbose_name_plural = 'Graphics'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
