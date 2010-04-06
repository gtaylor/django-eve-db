"""
Import certification data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_crtCategories(SQLImporter):
    def import_row(self, row):
        imp_obj, created = CrtCategory.objects.get_or_create(id=row['categoryID'])
        imp_obj.description = row['description']
        imp_obj.name = row['categoryName']
        imp_obj.save()
        
class Importer_crtClasses(SQLImporter):
    def import_row(self, row):
        imp_obj, created = CrtClass.objects.get_or_create(id=row['classID'])
        imp_obj.description = row['description']
        imp_obj.name = row['className']
        imp_obj.save()
        
class Importer_crtCertificates(SQLImporter):
    DEPENDENCIES = ['crtCategories', 'crtClasses', 'crpNPCCorporations']

    def import_row(self, row):
        imp_obj, created = CrtCertificate.objects.get_or_create(id=row['certificateID'])
        imp_obj.category = CrtCategory.objects.get(id=row['categoryID'])
        imp_obj.cert_class = CrtClass.objects.get(id=row['classID'])
        imp_obj.grade = row['grade']
        imp_obj.corporation = EVENPCCorporation.objects.get(id=row['corpID'])
        imp_obj.description = row['description']
        imp_obj.icon_num = row['iconID']
        imp_obj.save()
        
class Importer_crtRelationships(SQLImporter):
    DEPENDENCIES = ['invTypes', 'crtCertificates']

    def import_row(self, row):
        imp_obj, created = CrtRelationship.objects.get_or_create(id=row['relationshipID'])
        imp_obj.parent_level = row['parentLevel']
        imp_obj.child = CrtCertificate.objects.get(id=row['childID'])
        
        if row['parentID']:
            imp_obj.parent = CrtCertificate.objects.get(id=row['parentID'])
        
        if row['parentTypeID']:
            imp_obj.parent_type = EVEInventoryType.objects.get(id=row['parentTypeID'])

        imp_obj.save()
        
class Importer_crtRecommendations(SQLImporter):
    DEPENDENCIES = ['invTypes', 'crtCertificates']

    def import_row(self, row):
        imp_obj, created = CrtRecommendation.objects.get_or_create(id=row['recommendationID'])
        imp_obj.ship_type = EVEInventoryType.objects.get(id=row['shipTypeID'])
        imp_obj.certificate = CrtCertificate.objects.get(id=row['certificateID'])
        imp_obj.recommendation_level = row['recommendationLevel']
        imp_obj.save()