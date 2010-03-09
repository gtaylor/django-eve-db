from django.db import models

class EVEResearchAndMfgActivity(models.Model):
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
    type = models.ForeignKey('EVEInventoryType', related_name='stationtype_set')
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
        return self.type.name
    
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