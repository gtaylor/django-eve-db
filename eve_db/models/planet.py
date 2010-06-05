"""
Tables related to Planetary Interaction
"""
from django.db import models

class PlanetSchematic(models.Model):
    """
    Schematics are the equivilent of blueprints or reactions for Planetary
    Interaction.  They control the rate and inputs/outputs of 
    
    CCP Table: planetSchematics
    CCP Primary Key: "schematicID"
    """
    
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    cycle_time = models.IntegerField(null=True, blank=True)
    
    """
    Many to Many Fields are not present in the CCP dump but allow django
    to naturally traverse the join tables.
    """
    pin_map = models.ManyToManyField('InvType', through='PlanetSchematicsPinMap', related_name='usable_schematics')
    type_map = models.ManyToManyField('Invtype', through='PlanetSchematicsTypeMap', related_name='used_with_schematic')    
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Planet Schematic'
        verbose_name_plural = 'Planet Schematics'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class PlanetSchematicsPinMap(models.Model):
    """
    This table links the schematics to a "pin."  A Pin is a building in
    Planetary Interaction.  Use this table to determine what type of schematics
    can be loaded into what type of building.
    
    CCP Table: planetSchematicsPinMap
    """
    
    schematic = models.ForeignKey(PlanetSchematic)
    type = models.ForeignKey('InvType')
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['schematic','type']
        unique_together = ("schematic", "type")
        verbose_name = 'Planet Schematic Pin Map'
        verbose_name_plural = 'Planet Schematic Pin Maps'
        
    def __unicode__(self):
        return self.schematic.name + ' ' + self.type.name
    
    def __str__(self):
        return self.__unicode__()


class PlanetSchematicsTypeMap(models.Model):
    """
    This table defines the input/output requirements for Planetary Interaction
    Schematics
    
    CCP Table: planetSchematicsTypeMap
    """
    
    schematic = models.ForeignKey(PlanetSchematic)
    type = models.ForeignKey('InvType')
    quantity = models.IntegerField(null=True, blank=True)
    is_input = models.BooleanField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['schematic', 'is_input', 'type']
        unique_together = ("schematic", "type")
        verbose_name = 'Planet Schematic Type Map'
        verbose_name_plural = 'Planet Schematic Type Maps'
        
    def __unicode__(self):
        return "%s - %s(%s)"  % (self.schematic.name, self.type.name, self.quantity)
    
    def __str__(self):
        return self.__unicode__()
