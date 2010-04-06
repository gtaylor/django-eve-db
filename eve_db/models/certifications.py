"""
Skill-based certification models.
"""
from django.db import models

class CrtCategory(models.Model):
    """
    crtCategories
    """
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Certification Category'
        verbose_name_plural = 'Certification Categories'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class CrtClass(models.Model):
    """
    crtClasses
    """
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Certification Class'
        verbose_name_plural = 'Certification Classes'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class CrtCertificate(models.Model):
    """
    CrtCertificate
    """
    category = models.ForeignKey(CrtCategory, blank=True, null=True)
    # Can't call this 'class', that's a reserved keyword.
    cert_class = models.ForeignKey(CrtClass, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    corporation = models.ForeignKey('CrpNPCCorporation', blank=True, null=True)
    # Is this similar to the icon_filename fields on other models? The format
    # is different in the CCP dump.
    icon_num = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
        
    def __unicode__(self):
        return "%s, grade %d" % (self.cert_class.name, self.grade)
    
    def __str__(self):
        return self.__unicode__()
    
class CrtRelationship(models.Model):
    """
    crtRelationships
    """
    parent = models.ForeignKey(CrtCertificate, blank=True, null=True,
                               related_name='parent_crtrelationship_set')
    parent_type = models.ForeignKey('InvType', blank=True, null=True)
    parent_level = models.IntegerField(blank=True, null=True)
    child = models.ForeignKey(CrtCertificate, blank=True, null=True,
                              related_name='child_crtrelationship_set')
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Certification Relationship'
        verbose_name_plural = 'Certification Relationships'
        
    def __unicode__(self):
        return "Cert Relationship: %d" % self.id
    
    def __str__(self):
        return self.__unicode__()
    
class CrtRecommendation(models.Model):
    """
    crtRecommendations
    """
    ship_type = models.ForeignKey('InvType', blank=True, null=True)
    certificate = models.ForeignKey(CrtCertificate, blank=True, null=True)
    recommendation_level = models.IntegerField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Certification Recommendation'
        verbose_name_plural = 'Certification Recommendations'
        
    def __unicode__(self):
        return "%s: %s" % (self.ship_type.name, 
                           self.certificate.cert_class.name)
    
    def __str__(self):
        return self.__unicode__()