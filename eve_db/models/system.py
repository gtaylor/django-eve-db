"""
Critical components that are used throughout the other modules.
"""
from django.db import models

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
