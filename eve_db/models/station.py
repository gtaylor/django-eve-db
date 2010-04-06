from django.db import models

class EVERamActivity(models.Model):
    """
    Research and Manufacturing activities.
    """
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
    
class EVERamAssemblyLineType(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    base_time_multiplier = models.FloatField(blank=True, null=True)
    base_material_multiplier = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    activity = models.ForeignKey(EVERamActivity, blank=True, null=True)
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
    
class EVERamAssemblyLine(models.Model):
    """
    ramAssemblyLines
    """
    # Just a denormalized assembly_line_type.name.
    name = models.CharField(max_length=255, blank=True)
    assembly_line_type = models.ForeignKey(EVERamAssemblyLineType, blank=True,
                                           null=True)
    station = models.ForeignKey('EVEStation', blank=True, null=True)
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
    owner = models.ForeignKey('EVENPCCorporation', blank=True, null=True)
    activity = models.ForeignKey('EVERamActivity', blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line'
        verbose_name_plural = 'Assembly Lines'
        
    def __unicode__(self):
        return self.assembly_line_type
    
    def __str__(self):
        return self.__unicode__()
    
class EVERamAssemblyLineTypeDetailPerCategory(models.Model):
    assembly_line_type = models.ForeignKey(EVERamAssemblyLineType)
    category = models.ForeignKey('EVEInventoryCategory')
    time_multiplier = models.FloatField(blank=True, null=True)
    material_multiplier = models.FloatField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line Detail per Category'
        verbose_name_plural = 'Assembly Line Details per Category'
        
    def __unicode__(self):
        return self.assembly_line_type.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVERamAssemblyLineTypeDetailPerGroup(models.Model):
    assembly_line_type = models.ForeignKey(EVERamAssemblyLineType)
    group = models.ForeignKey('EVEInventoryGroup')
    time_multiplier = models.FloatField(blank=True, null=True)
    material_multiplier = models.FloatField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line Detail per Group'
        verbose_name_plural = 'Assembly Line Details per Group'
        
    def __unicode__(self):
        return self.assembly_line_type.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVERamAssemblyLineStations(models.Model):
    station = models.ForeignKey('EVEStation')
    assembly_line_type = models.ForeignKey('EVERamAssemblyLineType')
    quantity = models.IntegerField(blank=True, null=True)
    station_type = models.ForeignKey('EVEStationType', blank=True, null=True)
    owner = models.ForeignKey('EVENPCCorporation', blank=True, null=True)
    solar_system = models.ForeignKey('EVESolarSystem', blank=True, null=True)
    region = models.ForeignKey('EVERegion', blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Assembly Line Station'
        verbose_name_plural = 'Assembly Line Stations'
        
    def __unicode__(self):
        return "%s: %s" % (self.station, self.assembly_line_type.name)
    
    def __str__(self):
        return self.__unicode__()

class EVEStationService(models.Model):
    """
    staServices
    """
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

class EVEStationType(models.Model):
    """
    staStationTypes
    """
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
    operation = models.ForeignKey('EVEStationOperation', blank=True, null=True)
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

class EVEStationOperation(models.Model):
    """
    staOperations
    """
    activity_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    ratio = models.IntegerField(blank=True, null=True)
    caldari_station_type = models.ForeignKey(EVEStationType,
                                             related_name='caldari_station_operation_set', 
                                             blank=True, null=True)
    minmatar_station_type = models.ForeignKey(EVEStationType,
                                              related_name='minmatar_station_operation_set', 
                                              blank=True, null=True)
    amarr_station_type = models.ForeignKey(EVEStationType,
                                           related_name='amarr_station_operation_set', 
                                           blank=True, null=True)
    gallente_station_type = models.ForeignKey(EVEStationType,
                                              related_name='gallente_station_operation_set', 
                                              blank=True, null=True)
    jove_station_type = models.ForeignKey(EVEStationType,
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
        
class EVEStation(models.Model):
    """
    staStations
    """
    security = models.IntegerField(blank=True, null=True)
    docking_cost_per_volume = models.FloatField(blank=True, null=True)
    max_ship_volume_dockable = models.FloatField(blank=True, null=True)
    office_rental_cost = models.IntegerField(blank=True, null=True)
    operation = models.ForeignKey(EVEStationOperation, blank=True, null=True)
    type = models.ForeignKey(EVEStationType, blank=True, null=True)
    corporation = models.ForeignKey('EVENPCCorporation', blank=True, null=True)
    solar_system = models.ForeignKey('EVESolarSystem', blank=True, null=True)
    constellation = models.ForeignKey('EVEConstellation', blank=True, null=True)
    region = models.ForeignKey('EVERegion', blank=True, null=True)
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
    
class EVEStationOperationServices(models.Model):
    """
    staOperationServices
    
    Services per operations. 
    """
    operation = models.ForeignKey(EVEStationOperation)
    service = models.ForeignKey(EVEStationService)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Station Operation Service'
        verbose_name_plural = 'Station Operation Services'
        
    def __unicode__(self):
        return "%s: %s" % (self.operation, self.service)
    
    def __str__(self):
        return self.__unicode__()