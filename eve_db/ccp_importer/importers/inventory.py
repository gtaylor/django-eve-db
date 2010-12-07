"""
Import inventory data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_invCategories(SQLImporter):
    DEPENDENCIES = ['eveIcons']

    def import_row(self, row):
        category, created = InvCategory.objects.get_or_create(id=row['categoryID'])
        category.name = row['categoryName']
        category.description = row['description']

        icon_id = row['iconID']
        if icon_id:
            category.icon_id = EveIcon.objects.get(id=icon_id)

        # Handle boolean.
        if row['published'] != 1:
            category.is_published = False

        category.save()

class Importer_invGroups(SQLImporter):
    DEPENDENCIES = ['eveIcons', 'invCategories']

    def import_row(self, row):
        group = InvGroup(id=row['groupID'])
        group.category_id = row['categoryID']
        group.name = row['groupName']
        group.description = row['description']

        if row['iconID']:
            group.icon_id = row['iconID']

        # Handle boolean.
        group.use_base_price = self.parse_int_bool(row['useBasePrice'])
        group.allow_manufacture = self.parse_int_bool(row['allowManufacture'])
        group.allow_recycle = self.parse_int_bool(row['allowRecycler'])
        group.allow_anchoring = self.parse_int_bool(row['anchorable'])
        group.is_anchored = self.parse_int_bool(row['anchored'])
        group.is_fittable_non_singleton = self.parse_int_bool(row['fittableNonSingleton'])
        group.is_published = self.parse_int_bool(row['published'])

        group.save()

class Importer_invMetaGroups(SQLImporter):
    DEPENDENCIES = ['eveIcons']

    def import_row(self, row):
        imp_obj, created = InvMetaGroup.objects.get_or_create(id=row['metaGroupID'])
        imp_obj.name = row['metaGroupName']
        imp_obj.description = row['description']

        icon_id = row['iconID']
        if icon_id:
            imp_obj.icon = EveIcon.objects.get(id=icon_id)

        imp_obj.save()

class Importer_invMarketGroups(SQLImporter):
    DEPENDENCIES = ['eveIcons', 'invMarketGroups']

    def import_row(self, row):
        group = InvMarketGroup(id=row['marketGroupID'])
        group.name = row['marketGroupName']
        group.description = row['description']

        if row['iconID']:
            group.icon_id = row['iconID']

        if row['parentGroupID']:
            group.parent_id = row['parentGroupID']

        group.has_items = self.parse_int_bool(row['hasTypes'])
        group.save()

class Importer_invTypes(SQLImporter):
    DEPENDENCIES = ['eveGraphics', 'eveIcons', 'invMarketGroups', 'chrRaces',
                    'invGroups']

    def import_row(self, row):
        invtype = InvType(id=row['typeID'])
        invtype.name = row['typeName']
        invtype.description = row['description']
        invtype.group_id = row['groupID']
        invtype.radius = row['radius']
        invtype.mass = row['mass']
        invtype.volume = row['volume']
        invtype.capacity = row['capacity']
        invtype.portion_size = row['portionSize']
        invtype.base_price = row['basePrice']

        if row['marketGroupID']:
            invtype.market_group_id = row['marketGroupID']

        if row['published'] == 1:
            invtype.is_published = True

        if row['raceID']:
            invtype.race_id = row['raceID']

        if row['graphicID']:
            invtype.graphic_id = row['graphicID']

        if row['iconID']:
            invtype.icon_id = row['iconID']

        invtype.chance_of_duplicating = row['chanceOfDuplicating']
        invtype.save()

class Importer_invTypeMaterials(SQLImporter):
    DEPENDENCIES = ['invTypes']

    def import_row(self, row):
        item_type = InvType(id=row['typeID'])
        material_type = InvType(id=row['materialTypeID'])
        invmat, created = InvTypeMaterial.objects.get_or_create(type=item_type,
                                                                material_type=material_type)
        invmat.quantity = row['quantity']
        invmat.save()
        
    def import_new_row(self, row):
        invmat = InvTypeMaterial(type_id=row['typeID'],
                                 material_type_id=row['materialTypeID'],
                                 quantity=row['quantity'])
        invmat.save()

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

    def import_row(self, row):
        imp_obj, created = InvFlag.objects.get_or_create(id=row['flagID'])
        imp_obj.name = row['flagName']
        imp_obj.text = row['flagText']
        imp_obj.type_text = row['flagType']
        imp_obj.order = row['orderID']
        imp_obj.save()

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

    def import_row(self, row):
        imp_obj, created = InvPOSResourcePurpose.objects.get_or_create(id=row['purpose'])
        imp_obj.purpose = row['purposeText']
        imp_obj.save()

class Importer_invControlTowerResources(SQLImporter):
    DEPENDENCIES = ['invTypes', 'invControlTowerResourcePurposes']

    def import_row(self, row):
        control_tower_type = InvType(id=row['controlTowerTypeID'])
        resource_type = InvType(id=row['resourceTypeID'])
        imp_obj, created = InvPOSResource.objects.get_or_create(control_tower_type=control_tower_type,
                                                                resource_type=resource_type)
        imp_obj.control_tower_type = control_tower_type
        imp_obj.resource_type = resource_type
        imp_obj.purpose_id = row['purpose']
        imp_obj.quantity = row['quantity']
        imp_obj.min_security_level = row['minSecurityLevel']
        imp_obj.save()

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
