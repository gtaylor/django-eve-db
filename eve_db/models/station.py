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

class StationService(models.Model):
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