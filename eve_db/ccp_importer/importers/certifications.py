"""
Import certification data.
"""
from eve_db.models import certifications
from importer_classes import SQLImporter

class Importer_crtCategories(SQLImporter):
    model = certifications.CrtCategory
    pks = (('id', 'categoryID'),)
    field_map = (('description', 'description'),
                 ('name', 'categoryName'))


class Importer_crtClasses(SQLImporter):
    model = certifications.CrtClass
    pks = (('id', 'classID'),)
    field_map = (('description', 'description'),
                 ('name', 'className'))


class Importer_crtCertificates(SQLImporter):
    DEPENDENCIES = ['crtCategories', 'crtClasses', 'crpNPCCorporations']
    model = certifications.CrtCertificate
    pks = (('id', 'certificateID'),)
    field_map = (('category_id', 'categoryID'),
                 ('cert_class_id', 'classID'),
                 ('grade', 'grade'),
                 ('corporation_id', 'corpID'),
                 ('description', 'description'),
                 ('icon_num', 'iconID'))


class Importer_crtRelationships(SQLImporter):
    DEPENDENCIES = ['invTypes', 'crtCertificates']
    model = certifications.CrtRelationship
    pks = (('id', 'relationshipID'),)
    field_map = (('parent_level', 'parentLevel'),
                 ('child_id', 'childID'),
                 ('parent_id', 'parentID'),
                 ('parent_type_id', 'parentTypeID'))


class Importer_crtRecommendations(SQLImporter):
    DEPENDENCIES = ['invTypes', 'crtCertificates']
    model = certifications.CrtRecommendation
    pks = (('id', 'recommendationID'),)
    field_map = (('ship_type_id', 'shipTypeID'),
                 ('certificate_id', 'certificateID'),
                 ('recommendation_level', 'recommendationLevel'))
