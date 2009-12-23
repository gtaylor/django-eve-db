"""
NPC Corporations, agents, and other fun.
"""
from django.db import models

class CorporateActivity(models.Model):
    """
    crpActivities
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Corporate Activity'
        verbose_name_plural = 'Corporate Activities'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class NPCCorporation(models.Model):
    """
    crpNPCCorporations
    """
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    
    CORP_SIZE_CHOICES = (('H', 'Huge'),
                         ('L', 'Large'),
                         ('M', 'Medium'),
                         ('S', 'Small'),
                         ('T', 'Tiny'))

    size = models.CharField(choices=CORP_SIZE_CHOICES, max_length=1, 
                            blank=True)
    
    EXTENT_CHOICES = (('G', 'Global'),
                      ('N', 'National'),
                      ('R', 'Regional'),
                      ('C', 'Constellational'),
                      ('L', 'Local'))
    extent = models.CharField(choices=EXTENT_CHOICES, max_length=1,
                              blank=True)
    
    solar_system = models.ForeignKey('SolarSystem', blank=True, null=True)
    investor1 = models.ForeignKey('self', blank=True, null=True,
                                  related_name='invested1_set')
    investor1_shares = models.IntegerField(blank=True, null=True)
    investor2 = models.ForeignKey('self', blank=True, null=True,
                                  related_name='invested2_set')
    investor2_shares = models.IntegerField(blank=True, null=True)
    investor3 = models.ForeignKey('self', blank=True, null=True,
                                  related_name='invested3_set')
    investor3_shares = models.IntegerField(blank=True, null=True)
    investor4 = models.ForeignKey('self', blank=True, null=True,
                                  related_name='invested4_set')
    investor4_shares = models.IntegerField(blank=True, null=True)
    friendly_corp = models.ForeignKey('self', blank=True, null=True,
                                      related_name='friendly_with_set')
    enemy_corp = models.ForeignKey('self', blank=True, null=True,
                                   related_name='enemy_of_set')
    public_share_percent = models.FloatField(blank=True, null=True)
    initial_share_price = models.IntegerField(blank=True, null=True)
    min_security = models.FloatField(blank=True, null=True)
    stations_are_scattered = models.BooleanField(default=False)
    fringe_systems = models.IntegerField(default=0)
    corridor_systems = models.IntegerField(default=0)
    hub_systems = models.IntegerField(default=0)
    border_systems = models.IntegerField(default=0)
    faction = models.ForeignKey('EVEFaction', blank=True, null=True)
    size_factor = models.FloatField(blank=True, null=True)
    station_count = models.IntegerField(default=0)
    station_system_count = models.IntegerField(default=0)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'NPC Corporation'
        verbose_name_plural = 'NPC Corporations'
        
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Corporation #%d" % self.id
    
    def __str__(self):
        return self.__unicode__()

class NPCCorporationDivision(models.Model):
    """
    Used for NPC agents.
    
    crpNPCDivisions
    """
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    leader_type = models.CharField(max_length=100, blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'NPC Corporation Division'
        verbose_name_plural = 'NPC Corporation Division'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()