"""
NPC Corporations, agents, and other fun.
"""
from django.db import models

class CrpActivity(models.Model):
    """
    Activity types of corporations. 
    
    CCP Table: crpActivities
    CCP Primary key: "activityID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
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

class CrpNPCCorporation(models.Model):
    """
    CCP Table: crpNPCCorporations
    CCP Primary key: "corporationID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
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

    solar_system = models.ForeignKey('MapSolarSystem', blank=True, null=True)
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
    faction = models.ForeignKey('ChrFaction', blank=True, null=True)
    size_factor = models.FloatField(blank=True, null=True)
    station_count = models.IntegerField(default=0)
    station_system_count = models.IntegerField(default=0)
    icon = models.ForeignKey('EveIcon', blank=True, null=True)

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

class CrpNPCDivision(models.Model):
    """
    Agent division types.
    
    CCP Table: crpNPCDivisions
    CCP Primary key: "divisionID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    leader_type = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'NPC Division'
        verbose_name_plural = 'NPC Divisions'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class CrpNPCCorporationDivision(models.Model):
    """
    Agent divisions available in corporations.
    
    CCP Table: crpNPCCorporationDivisions
    CCP Primary key: ("corporationID" int(11), "divisionID" tinyint(3))
    """
    corporation = models.ForeignKey(CrpNPCCorporation)
    division = models.ForeignKey(CrpNPCDivision)
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'NPC Corporation Division'
        verbose_name_plural = 'NPC Corporation Divisions'
        unique_together = ('corporation', 'division')

    def __unicode__(self):
        return "%s: %s" % (self.corporation, self.division)

    def __str__(self):
        return self.__unicode__()

class CrpNPCCorporationTrade(models.Model):
    """
    Market items the corporation buys or sells. Supply/demand has been removed 
    from dumps, see:
    http://www.eveonline.com/ingameboard.asp?a=topic&threadID=835467&page=2#32. 
    
    CCP Table: crpNPCCorporationTrades
    CCP Primary key: ("corporationID" int(11), "typeID" smallint(6))
    """
    corporation = models.ForeignKey(CrpNPCCorporation)
    type = models.ForeignKey('InvType', blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'NPC Corporation Trade'
        verbose_name_plural = 'NPC Corporation Trades'
        unique_together = ('corporation', 'type')

    def __unicode__(self):
        return "%s: %s" % (self.corporation, self.type)

    def __str__(self):
        return self.__unicode__()

class CrpNPCCorporationResearchField(models.Model):
    """
    Research fields for R&D agents in corporations. 
    
    CCP Table: crpNPCCorporationResearchFields
    CCP Primary key: ("skillID" smallint(6), "corporationID" int(11))
    """
    corporation = models.ForeignKey(CrpNPCCorporation)
    skill = models.ForeignKey('InvType', blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'NPC Corporation Research Field'
        verbose_name_plural = 'NPC Corporation Research Fields'
        unique_together = ('skill', 'corporation')

    def __unicode__(self):
        return "%s: %s" % (self.corporation, self.skill)

    def __str__(self):
        return self.__unicode__()

class AgtAgentType(models.Model):
    """
    CCP Table: agtAgentTypes
    CCP Primary key: "agentTypeID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Agent Type'
        verbose_name_plural = 'Agent Types'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class AgtAgent(models.Model):
    """
    CCP Table: agtAgents
    CCP Primary key: "agentID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    division = models.ForeignKey(CrpNPCDivision, blank=True,
                                 null=True)
    corporation = models.ForeignKey(CrpNPCCorporation, blank=True, null=True)
    location = models.ForeignKey('MapDenormalize', blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey(AgtAgentType, blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
