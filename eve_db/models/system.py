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
    
    eveNames
    """
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

class EVEUnit(models.Model):
    """
    Units of measurement.
    
    eveUnits
    """
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
    
class EVEGraphic(models.Model):
    """
    Stored graphic model.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    # Name of the file, should be two numbers separated by underscore, no extension.
    icon_filename = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
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