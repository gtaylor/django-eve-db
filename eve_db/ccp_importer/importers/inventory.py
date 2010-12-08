"""
Import inventory data.
"""
from eve_db.models import *
from importer_classes import SQLImporter, parse_int_bool



class Importer_invCategories(SQLImporter):
    DEPENDENCIES = ['eveIcons']
    model = InvCategory
    pks = (('id', 'categoryID'),)
    field_map = (('name', 'categoryName'),
                 ('icon_id', 'iconID'),
                 ('description', 'description'),
                 ('is_published', 'published', parse_int_bool))


class Importer_invGroups(SQLImporter):
    DEPENDENCIES = ['eveIcons', 'invCategories']
    model = InvGroup
    pks = (('id', 'groupID'),)
    field_map = (('name', 'groupName'),
                 ('category_id', 'categoryID'),
                 ('description', 'description'),
                 ('icon_id', 'iconID'),
                 ('use_base_price', 'useBasePrice', parse_int_bool),
                 ('allow_manufacture', 'allowManufacture', parse_int_bool),
                 ('allow_recycle', 'allowRecycler', parse_int_bool),
                 ('allow_anchoring', 'anchorable', parse_int_bool),
                 ('is_anchored', 'anchored', parse_int_bool),
                 ('is_fittable_non_singleton', 'fittableNonSingleton', parse_int_bool),
                 ('is_published', 'published', parse_int_bool))


class Importer_invMetaGroups(SQLImporter):
    DEPENDENCIES = ['eveIcons']
    model = InvMetaGroup
    pks = (('id', 'metaGroupID'),)
    field_map = (('name', 'metaGroupName'),
                 ('icon_id', 'iconID'),
                 ('description', 'description'))


class Importer_invMarketGroups(SQLImporter):
    DEPENDENCIES = ['eveIcons', 'invMarketGroups']
    model = InvMarketGroup
    pks = (('id', 'marketGroupID'),)
    field_map = (('name', 'marketGroupName'),
                 ('icon_id', 'iconID'),
                 ('description', 'description'),
                 ('parent_id', 'parentGroupID'),
                 ('has_items', 'hasTypes', parse_int_bool))


class Importer_invTypes(SQLImporter):
    DEPENDENCIES = ['eveGraphics', 'eveIcons', 'invMarketGroups', 'chrRaces',
                    'invGroups']
    model = InvType
    pks = (('id', 'typeID'),)
    field_map = (('name', 'typeName'),
                 ('description', 'description'),
                 ('group_id', 'groupID'),
                 ('radius', 'radius'),
                 ('mass', 'mass'),
                 ('volume', 'volume'),
                 ('capacity', 'capacity'),
                 ('portion_size', 'portionSize'),
                 ('base_price', 'basePrice'),
                 ('market_group_id', 'marketGroupID'),
                 ('is_published', 'published', parse_int_bool),
                 ('race_id', 'raceID'),
                 ('graphic_id', 'graphicID'),
                 ('icon_id', 'iconID'),
                 ('chance_of_duplicating', 'chanceOfDuplicating'))


class Importer_invTypeMaterials(SQLImporter):
    DEPENDENCIES = ['invTypes']
    model = InvTypeMaterial
    pks = (('type', 'typeID'), ('material_type', 'materialTypeID'))
    field_map = (('quantity', 'quantity'),)


class Importer_invMetaTypes(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invMetaGroups']

    def import_row(self, row):
        imp_obj = InvMetaType(type_id=row['typeID'],
                              parent_type_id=row['parentTypeID'],
                              meta_group_id=row['metaGroupID'])
        imp_obj.save()

class Importer_dgmAttributeCategories(SQLImporter):
    def import_row(self, row):
        imp_obj, created = DgmAttributeCategory.objects.get_or_create(id=row['categoryid'])
        imp_obj.name = row['categoryname']
        imp_obj.description = row['categorydescription']
        imp_obj.save()

class Importer_dgmAttributeTypes(SQLImporter):
    DEPENDENCIES = ['dgmAttributeCategories', 'eveIcons', 'eveUnits']

    def import_row(self, row):
        imp_obj = DgmAttributeType(id=row['attributeid'])
        imp_obj.name = row['attributename']
        imp_obj.description = row['description']
        imp_obj.default_value = row['defaultvalue']
        imp_obj.is_published = self.parse_int_bool(row['published'])
        imp_obj.display_name = row['displayname']
        imp_obj.is_stackable = self.parse_int_bool(row['stackable'])
        imp_obj.high_is_good = self.parse_int_bool(row['highisgood'])

        if row['categoryid']:
            imp_obj.category_id = row['categoryid']

        if row['unitid']:
            imp_obj.unit_id = row['unitid']

        if row['iconID']:
            imp_obj.icon_id = row['iconID']

        imp_obj.save()

class Importer_dgmTypeAttributes(SQLImporter):
    DEPENDENCIES = ['invTypes', 'dgmAttributeTypes', 'dgmTypeAttributes']

    def import_row(self, row):
        imp_obj, created = DgmTypeAttribute.objects.\
            get_or_create(inventory_type=InvType(id=row['typeid']),
                          attribute=DgmAttributeType(id=row['attributeid']))

        if row['valueint']:
            imp_obj.value_int = row['valueint']

        if row['valuefloat']:
            imp_obj.value_float = row['valuefloat']

        imp_obj.save()

class Importer_dgmEffects(SQLImporter):
    DEPENDENCIES = ['eveIcons', 'dgmAttributeTypes']

    def import_row(self, row):
        imp_obj = DgmEffect(id=row['effectID'],
                            name=row['effectName'],
                            category=row['effectCategory'],
                            pre_expression=row['preExpression'],
                            post_expression=row['postExpression'],
                            description=row['description'],
                            guid=row['guid'] if row['guid'] else '',
                            icon_id=row['iconID'],
                            is_offensive=self.parse_int_bool(row['isOffensive']),
                            is_assistance=self.parse_int_bool(row['isAssistance']),
                            duration_attribute_id=row['durationAttributeID'],
                            tracking_speed_attribute_id=row['trackingSpeedAttributeID'],
                            discharge_attribute_id=row['dischargeAttributeID'],
                            range_attribute_id=row['rangeAttributeID'],
                            falloff_attribute_id=row['falloffAttributeID'],
                            disallow_auto_repeat=self.parse_int_bool(row['disallowAutoRepeat']),
                            is_published=self.parse_int_bool(row['published']),
                            display_name=row['displayName'],
                            is_warp_safe=self.parse_int_bool(row['isWarpSafe']),
                            has_range_chance=self.parse_int_bool(row['rangeChance']),
                            has_electronic_chance=self.parse_int_bool(row['electronicChance']),
                            has_propulsion_chance=self.parse_int_bool(row['propulsionChance']),
                            distribution=row['distribution'],
                            sfx_name=row['sfxName'] if row['sfxName'] else '',
                            npc_usage_chance_attribute_id=row['npcUsageChanceAttributeID'],
                            npc_activation_chance_attribute_id=row['npcActivationChanceAttributeID'],
                            fitting_usage_chance_attribute_id=row['fittingUsageChanceAttributeID'])

        imp_obj.save()

class Importer_dgmTypeEffects(SQLImporter):
    DEPENDENCIES = ['invTypes', 'dgmEffects', 'dgmTypeEffects']

    def import_row(self, row):
        imp_obj, created = DgmTypeEffect.objects.\
            get_or_create(type=InvType(id=row['typeID']),
                          effect=DgmEffect(id=row['effectID']))
        imp_obj.is_default = row['isDefault']
        imp_obj.save()

class Importer_invFlags(SQLImporter):
    DEPENDENCIES = ['invFlags']
    model = InvFlag
    pks = (('id', 'flagID'),)
    field_map = (('name', 'flagName'),
                 ('text', 'flagText'),
                 ('order', 'orderID'))


class Importer_invBlueprintTypes(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invBlueprintTypes']

    def import_row(self, row):
        invtype = InvBlueprintType(blueprint_type_id=row['blueprintTypeID'],
                                   product_type_id=row['productTypeID'])
        if row['parentBlueprintTypeID']:
            invtype.parent_blueprint_type_id = row['parentBlueprintTypeID']

        invtype.tech_level = row['techLevel']
        invtype.research_productivity_time = row['researchProductivityTime']
        invtype.research_material_time = row['researchMaterialTime']
        invtype.research_copy_time = row['researchCopyTime']
        invtype.research_tech_time = row['researchTechTime']
        invtype.productivity_modifier = row['productivityModifier']
        invtype.material_modifier = row['materialModifier']
        invtype.waste_factor = row['wasteFactor']
        invtype.max_production_limit = row['maxProductionLimit']
        invtype.save()

class Importer_invControlTowerResourcePurposes(SQLImporter):
    DEPENDENCIES = ['invControlTowerResourcePurposes']
    model = InvPOSResourcePurpose
    pks = (('id', 'purpose'),)
    field_map = (('purpose', 'purposeText'),)


class Importer_invControlTowerResources(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invControlTowerResourcePurposes']
    model = InvPOSResource
    pks = (('control_tower_type', 'controlTowerTypeID'),
           ('resource_type', 'resourceTypeID'))
    field_map = (('purpose_id', 'purpose'),
                 ('quantity', 'quantity'),
                 ('min_security_level', 'minSecurityLevel'))


class Importer_invTypeReactions(SQLImporter):
    DEPENDENCIES = ['invTypes']

    def import_row(self, row):
        reaction_type = InvType.objects.get(id=row['reactionTypeID'])
        type = InvType.objects.get(id=row['typeID'])
        imp_obj, created = InvTypeReaction.objects.get_or_create(reaction_type=reaction_type,
                                                                           type=type)
        imp_obj.input = row['input']
        imp_obj.quantity = row['quantity']
        imp_obj.save()

class Importer_invContrabandTypes(SQLImporter):
    DEPENDENCIES = ['invTypes', 'chrFactions']

    def import_row(self, row):
        faction = ChrFaction.objects.get(id=row['factionID'])
        type = InvType.objects.get(id=row['typeID'])
        imp_obj, created = InvContrabandType.objects.get_or_create(faction=faction,
                                                                type=type)
        imp_obj.standing_loss = row['standingLoss']
        imp_obj.confiscate_min_sec = row['confiscateMinSec']
        imp_obj.fine_by_value = row['fineByValue']
        imp_obj.attack_min_sec = row['attackMinSec']

        imp_obj.save()
