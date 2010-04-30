from django.db import models

class RamActivity(models.Model):
    """
    Research and Manufacturing activities.
    
    CCP Table: ramActivities
    CCP Primary key: "activityID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=75, blank=True)
    description = models.CharField(max_length=100, blank=True)
    # Name of the file, should be two numbers separated by underscore, no extension.
    icon_filename = models.CharField(max_length=50, blank=True)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Research and Mfg activity'
        verbose_name_plural = 'Research and Mfg activities'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class RamAssemblyLineType(models.Model):
    """
    Various assembly line types.
    
    CCP Table: ramAssemblyLineTypes
    CCP Primary key: "assemblyLineTypeID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    base_time_multiplier = models.FloatField(blank=True, null=True)
    base_material_multiplier = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    activity = models.ForeignKey(RamActivity, blank=True, null=True)
    min_cost_per_hour = models.FloatField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line Type'
        verbose_name_plural = 'Assembly Line Types'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class RamAssemblyLine(models.Model):
    """
    These represent individual assembly lines in stations.
    
    CCP Table: ramAssemblyLines
    CCP Primary key: "assemblyLineID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    # Just a denormalized assembly_line_type.name.
    name = models.CharField(max_length=255, blank=True)
    assembly_line_type = models.ForeignKey(RamAssemblyLineType, blank=True,
                                           null=True)
    station = models.ForeignKey('StaStation', blank=True, null=True)
    ui_grouping_id = models.IntegerField(blank=True, null=True)
    cost_install = models.FloatField(blank=True, null=True)
    cost_per_hour = models.FloatField(blank=True, null=True)
    discount_per_good_standing_point = models.FloatField(blank=True, null=True)
    surcharge_per_bad_standing_point = models.FloatField(blank=True, null=True)
    minimum_standing = models.FloatField(blank=True, null=True)
    minimum_char_security = models.FloatField(blank=True, null=True)
    minimum_corp_security = models.FloatField(blank=True, null=True)
    maximum_char_security = models.FloatField(blank=True, null=True)
    maximum_corp_security = models.FloatField(blank=True, null=True)
    owner = models.ForeignKey('CrpNPCCorporation', blank=True, null=True)
    activity = models.ForeignKey('RamActivity', blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line'
        verbose_name_plural = 'Assembly Lines'
        
    def __unicode__(self):
        return self.assembly_line_type
    
    def __str__(self):
        return self.__unicode__()
    
class RamAssemblyLineTypeDetailPerCategory(models.Model):
    """
    Assembly line multipliers per produced item category. 
    
    CCP Table: ramAssemblyLineTypeDetailPerCategory
    CCP Primary key: ("assemblyLineTypeID" tinyint(3), "categoryID" tinyint(3))
    """
    assembly_line_type = models.ForeignKey(RamAssemblyLineType)
    category = models.ForeignKey('InvCategory')
    time_multiplier = models.FloatField(blank=True, null=True)
    material_multiplier = models.FloatField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line Detail per Category'
        verbose_name_plural = 'Assembly Line Details per Category'
        unique_together = ('assembly_line_type', 'category')
        
    def __unicode__(self):
        return self.assembly_line_type.name
    
    def __str__(self):
        return self.__unicode__()
    
class RamAssemblyLineTypeDetailPerGroup(models.Model):
    """
    Assembly line multipliers per produced item group. 
    
    CCP Table: ramAssemblyLineTypeDetailPerGroup
    CCP Primary key: ("assemblyLineTypeID" tinyint(3), "groupID" smallint(6))
    """
    assembly_line_type = models.ForeignKey(RamAssemblyLineType)
    group = models.ForeignKey('InvGroup')
    time_multiplier = models.FloatField(blank=True, null=True)
    material_multiplier = models.FloatField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line Detail per Group'
        verbose_name_plural = 'Assembly Line Details per Group'
        unique_together = ('assembly_line_type', 'group')
        
    def __unicode__(self):
        return self.assembly_line_type.name
    
    def __str__(self):
        return self.__unicode__()
    
class RamAssemblyLineStations(models.Model):
    """
    Denotes assembly line types on individual stations.
    
    CCP Table: ramAssemblyLineStations
    CCP Primary key: ("stationID" int(11), "assemblyLineTypeID" tinyint(3))
    """
    station = models.ForeignKey('StaStation')
    assembly_line_type = models.ForeignKey('RamAssemblyLineType')
    quantity = models.IntegerField(blank=True, null=True)
    station_type = models.ForeignKey('StaStationType', blank=True, null=True)
    owner = models.ForeignKey('CrpNPCCorporation', blank=True, null=True)
    solar_system = models.ForeignKey('MapSolarSystem', blank=True, null=True)
    region = models.ForeignKey('MapRegion', blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line Station'
        verbose_name_plural = 'Assembly Line Stations'
        unique_together = ('station', 'assembly_line_type')
        
    def __unicode__(self):
        return "%s: %s" % (self.station, self.assembly_line_type.name)
    
    def __str__(self):
        return self.__unicode__()

class RamTypeRequirement(models.Model):
    """
    CCP Table: ramTypeRequirements
    CCP Primary key: ("typeID" smallint(6), "activityID" tinyint(3), "requiredTypeID" smallint(6))
    """
    type = models.ForeignKey('InvType', related_name='type_requirement')
    activity_type = models.ForeignKey('RamActivity')
    required_type = models.ForeignKey('InvType', related_name='required_type')
    quantity = models.IntegerField(blank=True, null=True)
    damage_per_job = models.FloatField(blank=True, null=True)
    recycle = models.BooleanField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Type Requirement'
        verbose_name_plural = 'Type Requirements'
        unique_together = ('type', 'activity_type', 'required_type')
        
    def __unicode__(self):
        return "%s: %s (%s)" % (self.type.name, self.required_type.name, self.activity_type.name)
        
    def __str__(self):
        return self.__unicode__()


class StaService(models.Model):
    """
    Entries for all services available at stations.
    
    CCP Table: staServices
    CCP Primary key: "serviceID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Station Service'
        verbose_name_plural = 'Station Services'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class StaStationType(models.Model):
    """
    Details for the different types of stations.
    
    CCP Table: staStationTypes
    CCP Primary key: "stationTypeID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    docking_bay_graphic = models.ForeignKey('EVEGraphic',
                                            related_name='docking_bay_graphic', 
                                            blank=True, null=True)
    hangar_graphic = models.ForeignKey('EVEGraphic',
                                       related_name='hangar_graphic', 
                                       blank=True, null=True)
    dock_entry_x = models.FloatField(blank=True, null=True)
    dock_orientation_x = models.FloatField(blank=True, null=True)
    dock_entry_y = models.FloatField(blank=True, null=True)
    dock_orientation_y = models.FloatField(blank=True, null=True)
    dock_entry_z = models.FloatField(blank=True, null=True)
    dock_orientation_z = models.FloatField(blank=True, null=True)
    operation = models.ForeignKey('StaOperation', blank=True, null=True)
    office_slots = models.IntegerField(blank=True, null=True)
    reprocessing_efficiency = models.FloatField(blank=True, null=True)
    is_conquerable = models.BooleanField(default=False)    
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Station Type'
        verbose_name_plural = 'Station Types'
        
    def __unicode__(self):
        return "Station Type %d" % self.id
    
    def __str__(self):
        return self.__unicode__()

class StaOperation(models.Model):
    """
    Operation types for stations. 
    
    CCP Table: staOperations
    CCP Primary key: "operationID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    activity_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    ratio = models.IntegerField(blank=True, null=True)
    caldari_station_type = models.ForeignKey(StaStationType,
                                             related_name='caldari_station_operation_set', 
                                             blank=True, null=True)
    minmatar_station_type = models.ForeignKey(StaStationType,
                                              related_name='minmatar_station_operation_set', 
                                              blank=True, null=True)
    amarr_station_type = models.ForeignKey(StaStationType,
                                           related_name='amarr_station_operation_set', 
                                           blank=True, null=True)
    gallente_station_type = models.ForeignKey(StaStationType,
                                              related_name='gallente_station_operation_set', 
                                              blank=True, null=True)
    jove_station_type = models.ForeignKey(StaStationType,
                                          related_name='jove_station_operation_set',
                                          blank=True, null=True)
    
  
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Station Operation'
        verbose_name_plural = 'Station Operations'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
        
class StaStation(models.Model):
    """
    Represents an individual station out in a system. 
    
    CCP Table: staStations
    CCP Primary key: "stationID" int(11)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    security = models.IntegerField(blank=True, null=True)
    docking_cost_per_volume = models.FloatField(blank=True, null=True)
    max_ship_volume_dockable = models.FloatField(blank=True, null=True)
    office_rental_cost = models.IntegerField(blank=True, null=True)
    operation = models.ForeignKey(StaOperation, blank=True, null=True)
    type = models.ForeignKey(StaStationType, blank=True, null=True)
    corporation = models.ForeignKey('CrpNPCCorporation', blank=True, null=True)
    solar_system = models.ForeignKey('MapSolarSystem', blank=True, null=True)
    constellation = models.ForeignKey('MapConstellation', blank=True, null=True)
    region = models.ForeignKey('MapRegion', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    reprocessing_efficiency = models.FloatField(blank=True, null=True)
    reprocessing_stations_take = models.FloatField(blank=True, null=True)
    reprocessing_hangar_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class StaOperationServices(models.Model):
    """
    Services per operations. 
    
    CCP Table: staOperationServices
    CCP Primary key: ("operationID" tinyint(3), "serviceID" int(11))
    """
    operation = models.ForeignKey(StaOperation)
    service = models.ForeignKey(StaService)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Station Operation Service'
        verbose_name_plural = 'Station Operation Services'
        unique_together = ('operation', 'service')
        
    def __unicode__(self):
        return "%s: %s" % (self.operation, self.service)
    
    def __str__(self):
        return self.__unicode__()
