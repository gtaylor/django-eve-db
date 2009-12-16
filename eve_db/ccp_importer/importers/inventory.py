"""
Import inventory data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_invCategories(SQLImporter):
    DEPENDENCIES = ['eveGraphics']
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from invCategories'):
            category, created = EVEInventoryCategory.objects.get_or_create(id=row['categoryID'])
            category.name = row['categoryName']
            category.description = row['description']
            
            graphic_id = row['graphicID']
            if graphic_id:
                category.graphic = EVEGraphic.objects.get(id=graphic_id)
                
            # Handle boolean.
            if row['published'] == 1:
                category.is_published = True
            else:
                category.is_published = False
    
            category.save()
        c.close()
    
class Importer_invGroups(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from invGroups'):
            category_id = row['categoryID']
            category = EVEInventoryCategory.objects.get(id=category_id)
    
            group, created = EVEInventoryGroup.objects.get_or_create(id=row['groupID'],
                                                                     category=category)
            group.name = row['groupName']
            group.description = row['description']
            
            graphic_id = row['graphicID']
            if graphic_id:
                group.graphic = EVEGraphic.objects.get(id=graphic_id)
                
            # Handle boolean.
            group.use_base_price = self.parse_int_bool(row['useBasePrice'])
            group.allow_manufacture = self.parse_int_bool(row['allowManufacture'])
            group.allow_recycle = self.parse_int_bool(row['allowRecycler'])
            group.allow_anchoring = self.parse_int_bool(row['anchorable'])
            group.is_anchored = self.parse_int_bool(row['anchored'])
            group.is_fittable_non_singleton = self.parse_int_bool(row['fittableNonSingleton'])
            group.is_published = self.parse_int_bool(row['published'])
    
            group.save()
        c.close()

class Importer_invMetaGroups(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from invMetaGroups'):
            imp_obj, created = EVEInventoryMetaGroup.objects.get_or_create(id=row['metaGroupID'])
            imp_obj.name = row['metaGroupName']
            imp_obj.description = row['description']
            
            graphic_id = row['graphicID']
            if graphic_id:
                imp_obj.graphic = EVEGraphic.objects.get(id=graphic_id)
            imp_obj.save()
        c.close()

class Importer_invMarketGroups(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from invMarketGroups'):
            group, created = EVEMarketGroup.objects.get_or_create(id=row['marketGroupID'])
            group.name = row['marketGroupName']
            group.description = row['description']
            
            graphic_id = row['graphicID']
            if graphic_id:
                group.graphic = EVEGraphic.objects.get(id=graphic_id)
                
            parent_id = row['parentGroupID']
            if parent_id:
                parent, created = EVEMarketGroup.objects.get_or_create(id=parent_id)
                group.parent = parent
                
            group.has_items = self.parse_int_bool(row['hasTypes'])
    
            group.save()
        c.close()
    
class Importer_invTypes(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from invTypes'):
            invtype, created = EVEInventoryType.objects.get_or_create(id=row['typeID'])
            invtype.name = row['typeName']
            invtype.description = row['description']
            invtype.group = EVEInventoryGroup.objects.get(id=row['groupID'])
            invtype.radius = row['radius']
            invtype.mass = row['mass']
            invtype.volume = row['volume']
            invtype.capacity = row['capacity']
            invtype.portion_size = row['portionSize']
            
            if row['marketGroupID']:
                invtype.market_group = EVEMarketGroup.objects.get(id=row['marketGroupID'])
            
            if row['published'] == 1:
                invtype.is_published = True
            
            if row['raceID']:
                invtype.race = EVERace.objects.get(id=row['raceID'])
                
            if row['graphicID']:
                #print row['graphicID']
                invtype.graphic = EVEGraphic.objects.get(id=row['graphicID'])
                
            invtype.chance_of_duplicating = row['chanceOfDuplicating']
            invtype.save()
        c.close()
    
class Importer_invMetaTypes(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from invMetaTypes'):
            type = EVEInventoryType.objects.get(id=row['typeID'])
            parent_type = EVEInventoryType.objects.get(id=row['parentTypeID'])
            meta_group = EVEInventoryMetaGroup.objects.get(id=row['metaGroupID'])
            
            imp_obj, created = EVEInventoryMetaType.objects.get_or_create(type=type,
                                                    parent_type=parent_type,
                                                    meta_group=meta_group)
            imp_obj.save()
        c.close()

class Importer_dgmAttributeCategories(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
    
        for row in c.execute('select * from dgmattributecategories'):
            imp_obj, created = EVEInventoryAttributeCategory.objects.get_or_create(id=row['categoryid'])
            imp_obj.name = row['categoryname']
            imp_obj.description = row['categorydescription']
    
            imp_obj.save()
        c.close()

class Importer_dgmAttributeTypes(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
    
        for row in c.execute('select * from dgmattributetypes'):
            imp_obj, created = EVEInventoryAttributeType.objects.get_or_create(id=row['attributeid'])
            imp_obj.name = row['attributename']
            imp_obj.description = row['description']
            imp_obj.default_value = row['defaultvalue']
            imp_obj.is_published = self.parse_int_bool(row['published'])
            imp_obj.display_name = row['displayname']
            imp_obj.is_stackable = self.parse_int_bool(row['stackable'])
            imp_obj.high_is_good = self.parse_int_bool(row['highisgood'])
    
            category_id = row['categoryid']
            if category_id:
                imp_obj.category = EVEInventoryAttributeCategory.objects.get(id=category_id)
    
            unit_id = row['unitid']
            if unit_id:
                imp_obj.unit = EVEUnit.objects.get(id=unit_id)
    
            graphic_id = row['graphicID']
            if graphic_id:
                imp_obj.graphic = EVEGraphic.objects.get(id=graphic_id)
    
            imp_obj.save()
        c.close()

class Importer_dgmTypeAttributes(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
    
        for row in c.execute('select * from dgmtypeattributes'):    
            inventory_type = EVEInventoryType.objects.get(id=row['typeid'])
            attribute = EVEInventoryAttributeType.objects.get(id=row['attributeid'])
            imp_obj, created = EVEInventoryTypeAttributes.objects.get_or_create(inventory_type=inventory_type,
                                                                                attribute=attribute)
    
            if row['valueint']:
                imp_obj.value_int = row['valueint']
    
            if row['valuefloat']:
                imp_obj.value_float = row['valuefloat']
    
            imp_obj.save()
        c.close()

    
class Importer_dgmEffects(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from dgmEffects'):
            imp_obj, created = EVEInventoryEffect.objects.get_or_create(id=row['effectID'])
            imp_obj.name = row['effectName']
            imp_obj.category = row['effectCategory']
            imp_obj.pre_expression = row['preExpression']
            imp_obj.post_expression = row['postExpression']
            imp_obj.description = row['description']
            
            if row['guid']:
                imp_obj.guid = row['guid']
            
            if row['graphicID']:
                imp_obj.graphic = EVEGraphic.objects.get(id=row['graphicID'])
                
            if row['isOffensive'] == 1:
                imp_obj.is_offensive = True
                
            if row['isAssistance'] == 1:
                imp_obj.is_assistance = True
                
            if row['durationAttributeID']:
                imp_obj.duration_attribute = EVEInventoryAttributeType.objects.get(id=row['durationAttributeID'])
                
            if row['trackingSpeedAttributeID']:
                imp_obj.tracking_speed_attribute = EVEInventoryAttributeType.objects.get(id=row['trackingSpeedAttributeID'])
                
            if row['dischargeAttributeID']:
                imp_obj.discharge_attribute = EVEInventoryAttributeType.objects.get(id=row['dischargeAttributeID'])
                
            if row['rangeAttributeID']:
                imp_obj.range_attribute = EVEInventoryAttributeType.objects.get(id=row['rangeAttributeID'])
                
            if row['falloffAttributeID']:
                imp_obj.falloff_attribute = EVEInventoryAttributeType.objects.get(id=row['falloffAttributeID'])            
                
            if row['disallowAutoRepeat'] == 1:
                imp_obj.disallow_autorepeat = True
                
            if row['published'] == 1:
                imp_obj.is_published = True
                
            imp_obj.display_name = row['displayName']
            
            if row['isWarpSafe'] == 1:
                imp_obj.is_warp_safe = True
                
            if row['rangeChance'] == 1:
                imp_obj.has_range_chance = True
                
            if row['electronicChance'] == 1:
                imp_obj.has_electronic_chance = True
                
            if row['propulsionChance'] == 1:
                imp_obj.has_propulsion_chance = True
                
            imp_obj.distribution = row['distribution']
            
            if row['sfxName']:
                imp_obj.sfx_name = row['sfxName']
            
            if row['npcUsageChanceAttributeID']:
                imp_obj.npc_usage_chance_attribute = EVEInventoryAttributeType.objects.get(id=row['npcUsageChanceAttributeID'])
        
            if row['npcActivationChanceAttributeID']:
                imp_obj.npc_activation_chance_attribute = EVEInventoryAttributeType.objects.get(id=row['npcActivationChanceAttributeID'])
    
            if row['fittingUsageChanceAttributeID']:
                imp_obj.fitting_usage_chance_attribute = EVEInventoryAttributeType.objects.get(id=row['fittingUsageChanceAttributeID'])
    
            imp_obj.save()
        c.close()
    
class Importer_dgmTypeEffects(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from dgmTypeEffects'):
            type = EVEInventoryType.objects.get(id=row['typeID'])
            effect = EVEInventoryEffect.objects.get(id=row['effectID'])        
            imp_obj, created = EVEInventoryTypeEffect.objects.get_or_create(
                                                                    type=type,
                                                                    effect=effect)
            imp_obj.is_default = row['isDefault']
            imp_obj.save()
        c.close()
    
class Importer_invFlags(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from invFlags'):        
            imp_obj, created = EVEInventoryFlag.objects.get_or_create(id=row['flagID'])
            imp_obj.name = row['flagName']
            imp_obj.text = row['flagText']
            imp_obj.type_text = row['flagType']
            imp_obj.order = row['orderID']
            imp_obj.save()
        c.close()
    
class Importer_invBlueprintTypes(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from invBlueprintTypes'):
            blueprint_type = EVEInventoryType.objects.get(id=row['blueprintTypeID'])
            product_type = EVEInventoryType.objects.get(id=row['productTypeID'])
            invtype, created = EVEInventoryBlueprintType.objects.get_or_create(blueprint_type=blueprint_type,
                                                                               product_type=product_type)
            if row['parentBlueprintTypeID']:
                invtype.parent_blueprint_Type = EVEInventoryType.objects.get(id=row['parentBlueprintTypeID'])
                
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
        c.close()
    
class Importer_invControlTowerResourcePurposes(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
    
        for row in c.execute('select * from invControlTowerResourcePurposes'):
            imp_obj, created = EVEPOSResourcePurpose.objects.get_or_create(id=row['purpose'])
            imp_obj.purpose = row['purposeText']
            imp_obj.save()
        c.close()
    
class Importer_invControlTowerResources(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
    
        for row in c.execute('select * from invControlTowerResources'):
            control_tower_type = EVEInventoryType.objects.get(id=row['controlTowerTypeID'])
            resource_type = EVEInventoryType.objects.get(id=row['resourceTypeID'])
            imp_obj, created = EVEPOSResource.objects.get_or_create(control_tower_type=control_tower_type,
                                                                    resource_type=resource_type)
            imp_obj.control_tower_type = control_tower_type
            imp_obj.resource_type = resource_type
            imp_obj.purpose = EVEPOSResourcePurpose.objects.get(id=row['purpose'])
            imp_obj.quantity = row['quantity']
            imp_obj.min_security_level = row['minSecurityLevel']
            imp_obj.save()
        c.close()
    
class Importer_invTypeReactions(SQLImporter):
    """
    Import POS reactions.
    """
    def run_importer(self, conn):
        c = conn.cursor()
    
        for row in c.execute('select * from invTypeReactions'):
            reaction_type = EVEInventoryType.objects.get(id=row['reactionTypeID'])
            type = EVEInventoryType.objects.get(id=row['typeID'])
            imp_obj, created = EVEInventoryTypeReactions.objects.get_or_create(reaction_type=reaction_type,
                                                                               type=type)
            imp_obj.input = row['input']
            imp_obj.quantity = row['quantity']
            
            imp_obj.save()
        c.close()
    
class Importer_invContrabandTypes(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
    
        for row in c.execute('select * from invContrabandTypes'):
            faction = Faction.objects.get(id=row['factionID'])
            type = EVEInventoryType.objects.get(id=row['typeID'])
            imp_obj, created = ContrabandType.objects.get_or_create(faction=faction,
                                                                    type=type)
            imp_obj.standing_loss = row['standingLoss']
            imp_obj.confiscate_min_sec = row['confiscateMinSec']
            imp_obj.fine_by_value = row['fineByValue']
            imp_obj.attack_min_sec = row['attackMinSec']
            
            imp_obj.save()
        c.close()