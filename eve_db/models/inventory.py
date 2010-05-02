"""
This module holds inventory/item-related models.
"""
from xml.dom import minidom
from django.db import models
    
class InvMarketGroup(models.Model):
    """
    Market groups are used to group items together in the market browser.
    
    CCP Table: invMarketGroups
    CCP Primary key: "marketGroupID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    parent = models.ForeignKey('InvMarketGroup', blank=True, null=True)
    has_items = models.BooleanField(default=True)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)

    def full_name(self, delimiter='/'):
        """ Return a full name, including parents, recursively """
        if self.parent:
            return self.parent.full_name() + delimiter + self.name
        else:
            return self.name

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Market Group'
        verbose_name_plural = 'Market Groups'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class InvCategory(models.Model):
    """
    Inventory categories are the top level classification for all items, be
    it planets, moons, modules, ships, or any other entity within the game
    that physically exists.
    
    CCP Table: invCategories
    CCP Primary key: "categoryID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Category'
        verbose_name_plural = 'Inventory Categories'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class InvGroup(models.Model):
    """
    Inventory groups are a further sub-classification within an 
    InvCategory. For example, the 'MapRegion' inventory group's
    category is 'Celestial'.
    
    CCP Table: invGroups
    CCP Primary key: "groupID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    category = models.ForeignKey(InvCategory, blank=True, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    use_base_price = models.BooleanField(default=False)
    allow_manufacture = models.BooleanField(default=True)
    allow_recycle = models.BooleanField(default=True)
    allow_anchoring = models.BooleanField(default=False)
    is_anchored = models.BooleanField(default=False)
    is_fittable_non_singleton = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Group'
        verbose_name_plural = 'Inventory Groups'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class InvMetaGroup(models.Model):
    """
    Names of variants of items.
    
    CCP Table: invMetaGroups
    CCP Primary key: "metaGroupID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Meta Group'
        verbose_name_plural = 'Inventory Meta Groups'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class InvType(models.Model):
    """
    Inventory types are generally objects that can be carried in your
    inventory (with the exception of suns, moons, planets, etc.) These are mostly
    market items, along with some basic attributes of each that are common
    to all items. 
    
    CCP Table: invTypes
    CCP Primary key: "typeID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    group = models.ForeignKey(InvGroup, blank=True, null=True)
    market_group = models.ForeignKey(InvMarketGroup, blank=True, null=True)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    portion_size = models.IntegerField(blank=True, null=True)
    race = models.ForeignKey('ChrRace', blank=True, null=True)
    base_price = models.FloatField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    chance_of_duplicating = models.FloatField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Type'
        verbose_name_plural = 'Inventory Types'
        
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Inventory Type #%d" % self.id
    
    def __str__(self):
        return self.__unicode__()
    
class InvTypeMaterial(models.Model):
    """
    These are materials required to produce an item type. Used for calculating
    build requirements.
    
    CCP Table: invTypeMaterials
    CCP Primary key: ("typeID" smallint(6), "materialTypeID" smallint(6))
    """
    type = models.ForeignKey(InvType, related_name='material_set')
    material_type = models.ForeignKey(InvType, 
                                      related_name='itemtype_set')
    quantity = models.IntegerField(default=0)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Type Material'
        verbose_name_plural = 'Inventory Type Materials'
        unique_together = ('type', 'material_type')
        
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "%s: (%dx %s)" % (self.type.name, self.quantity,
                                     self.material_type.name)
    
    def __str__(self):
        return self.__unicode__()
    
class InvMetaType(models.Model):
    """
    Relation between different variants of item (i.e. Tech-I, Faction, Tech-II). 
    These are not "meta-levels" of items used for calculate invention success. 
    For that information see Attribute metaLevel (attributeID=633) in table 
    dgmTypeAttributes linked with type in question.
    
    CCP Table: invMetaTypes
    CCP Primary key: "typeID" smallint(6)
    """
    type = models.ForeignKey(InvType,
                            unique=True, primary_key=True,
                            related_name='inventorymetatype_type_set')
    parent_type = models.ForeignKey(InvType, 
                            related_name='inventorymetatype_parent_type_set')
    meta_group = models.ForeignKey(InvMetaGroup) 
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['type']
        verbose_name = 'Inventory Meta Type'
        verbose_name_plural = 'Inventory Meta Types'
        
    def __unicode__(self):
        return self.meta_group.name
    
    def __str__(self):
        return self.__unicode__()
    
class InvFlag(models.Model):
    """
    The invFlags table is used to identify the location and/or status of an 
    item within an office, station, ship, module or other container for the 
    API calls APIv2 Char AssetList XML and APIv2 Corp AssetList XML. 
    
    CCP Table: invFlags
    CCP Primary key: "flagID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    # Short name for the flag.
    name = models.CharField(max_length=255)
    # Full, descriptive name for the flag.
    text = models.CharField(max_length=255, blank=True)
    # Very inconsistently used.
    type_text = models.CharField(max_length=255, blank=True)
    # Have no idea what this is.
    order = models.IntegerField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Flag'
        verbose_name_plural = 'Inventory Flags'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class DgmAttributeCategory(models.Model):
    """
    Attribute Categories and their descriptions. 
    
    CCP Table: dgmAttributeCategories
    CCP Primary key: "categoryID" tinyint(3)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Attribute Category'
        verbose_name_plural = 'Inventory Attribute Categories'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class DgmAttributeType(models.Model):
    """
    Names and descriptions of attributes. 
    
    CCP Table: dgmAttributeTypes
    CCP Primary key: "attributeID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=75)
    category = models.ForeignKey(DgmAttributeCategory, blank=True, null=True)
    description = models.TextField(blank=True)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    defaultvalue = models.IntegerField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    display_name = models.CharField(max_length=100, blank=True)
    unit = models.ForeignKey('EVEUnit', blank=True, null=True)
    is_stackable = models.BooleanField(default=False)
    high_is_good = models.BooleanField(default=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Attribute Type'
        verbose_name_plural = 'Inventory Attribute Types'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class DgmTypeAttribute(models.Model):
    """
    All attributes for items.
    
    CCP Table: dgmTypeAttributes
    CCP Primary key: ("typeID" smallint(6), "attributeID" smallint(6))
    """
    inventory_type = models.ForeignKey(InvType)
    attribute = models.ForeignKey(DgmAttributeType)
    value_int = models.IntegerField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Type Attribute'
        verbose_name_plural = 'Inventory Type Attributes'
        unique_together = ('inventory_type', 'attribute')

    def __unicode__(self):
        return self.inventory_type.name + ' - ' + self.attribute.name

    def __str__(self):
        return self.__unicode__()
    
class InvBlueprintType(models.Model):
    """
    Stores info about each kind of blueprint.
    
    CCP Table: invBlueprintTypes
    CCP Primary key: "blueprintTypeID" smallint(6)
    """
    blueprint_type = models.ForeignKey(InvType,
                                       unique=True, primary_key=True,
                                       related_name='blueprint_type_set')
    product_type = models.ForeignKey(InvType,
                                     related_name='blueprint_product_type_set')
    # This is used for T2. Not always populated.
    parent_blueprint_type = models.ForeignKey(InvType, blank=True,
                                              null=True,
                                              related_name='parent_blueprint_type_set')
    tech_level = models.IntegerField(blank=True, null=True)
    research_productivity_time = models.IntegerField(blank=True, null=True)
    research_material_time = models.IntegerField(blank=True, null=True)
    research_copy_time = models.IntegerField(blank=True, null=True)
    research_tech_time = models.IntegerField(blank=True, null=True)
    productivity_modifier = models.IntegerField(blank=True, null=True)
    material_modifier = models.IntegerField(blank=True, null=True)
    waste_factor = models.IntegerField(blank=True, null=True)
    max_production_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['blueprint_type']
        verbose_name = 'Inventory Blueprint Type'
        verbose_name_plural = 'Inventory Blueprint Types'
        
    def __unicode__(self):
        return "BP: %s" % self.product_type
    
    def __str__(self):
        return self.__unicode__()
    
class DgmEffect(models.Model):
    """
    Name and descriptions of effects.
    
    CCP Table: dgmTypeEffects
    CCP Primary key: "effectID" smallint(6)
    """
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=150)
    # Not sure what this is. Internal category of effect.
    category = models.IntegerField(blank=True, null=True)
    # Unknown
    pre_expression = models.IntegerField(blank=True, null=True)
    # Unknown
    post_expression = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    # Unknown
    guid = models.CharField(max_length=255, blank=True)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    # If True, applied to enemy.
    is_offensive = models.BooleanField(default=False)
    # If True, applied to ally.
    is_assistance = models.BooleanField(default=False)
    duration_attribute = models.ForeignKey(DgmAttributeType, 
                                           blank=True, null=True,
                                           related_name='inventoryeffectdurationeattribute')
    tracking_speed_attribute = models.ForeignKey(DgmAttributeType, 
                                                 blank=True, null=True,
                                                 related_name='inventoryeffecttrackingspeedattribute')
    discharge_attribute = models.ForeignKey(DgmAttributeType, 
                                            blank=True, null=True,
                                            related_name='inventoryeffectdischargeattribute')
    range_attribute = models.ForeignKey(DgmAttributeType, 
                                        blank=True, null=True,
                                        related_name='inventoryeffectrangeattribute')
    falloff_attribute = models.ForeignKey(DgmAttributeType, 
                                          blank=True, null=True,
                                          related_name='inventoryeffectfalloffattribute')
    disallow_auto_repeat = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    # Name of effect as displayed in game.
    display_name = models.CharField(max_length=255, blank=True)
    is_warp_safe = models.BooleanField(default=False)
    has_range_chance = models.BooleanField(default=False)
    has_electronic_chance = models.BooleanField(default=False)
    has_propulsion_chance = models.BooleanField(default=False)
    distribution = models.IntegerField(blank=True, null=True)
    sfx_name = models.CharField(max_length=100, blank=True)
    npc_usage_chance_attribute = models.ForeignKey(DgmAttributeType, 
                                                   blank=True, null=True,
                                                   related_name='inventoryeffectnpcusagechanceattribute')
    npc_activation_chance_attribute = models.ForeignKey(DgmAttributeType, 
                                                        blank=True, null=True,
                                                        related_name='inventoryeffectnpcactivationchanceattribute')
    fitting_usage_chance_attribute = models.ForeignKey(DgmAttributeType, 
                                                       blank=True, null=True,
                                                       related_name='inventoryeffectfittingusagechanceattribute')
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Effect'
        verbose_name_plural = 'Inventory Effects'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class DgmTypeEffect(models.Model):
    """
    Effects related to items. Effects are like boolean flags - if an item has
    an effect listed, it's subject to this effect with the specified
    parameters, listed as per the DgmEffect.
    
    CCP Table: dgmTypeEffects
    CCP Primary key: ("typeID" smallint(6), "effectID" smallint(6))
    """
    type = models.ForeignKey(InvType)
    effect = models.ForeignKey(DgmEffect)
    is_default = models.BooleanField(default=False)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Type Effect'
        verbose_name_plural = 'Inventory Type Effect'
        unique_together = ('type', 'effect')
        
    def __unicode__(self):
        return self.type
    
    def __str__(self):
        return self.__unicode__()
    
class InvPOSResourcePurpose(models.Model):
    """
    Types of tasks for which POS need resources, i.e. Online, Reinforced. 
    
    CCP Table: invControlTowerResourcePurposes
    CCP Primary key: "purpose" tinyint(4)
    """
    # The id field maps to the CCP column purpose
    id = models.IntegerField(unique=True, primary_key=True)
    # The purpose field maps to the CCP column purposeText
    purpose = models.CharField(max_length=75, blank=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'POS Resource Purpose'
        verbose_name_plural = 'POS Resource Purposes'
        
    def __unicode__(self):
        return self.purpose
    
    def __str__(self):
        return self.__unicode__()

class InvPOSResource(models.Model):
    """
    Fuel needed to support POSes. 
    
    CCP Table: invControlTowerResources
    CCP Primary key: ("controlTowerTypeID" smallint(6), "resourceTypeID" smallint(6))
    """
    control_tower_type = models.ForeignKey(InvType,
                                           related_name='tower_resource_set')
    resource_type = models.ForeignKey(InvType,
                                      related_name='pos_resource_set')
    purpose = models.ForeignKey(InvPOSResourcePurpose, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    min_security_level = models.IntegerField(blank=True, null=True)
    faction = models.ForeignKey('ChrFaction', blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'POS Resource'
        verbose_name_plural = 'POS Resources'
        unique_together = ('control_tower_type', 'resource_type')
        
    def __unicode__(self):
        return "POS Resource #%d" % self.id
    
    def __str__(self):
        return self.__unicode__()
    
class InvTypeReaction(models.Model):
    """
    Reaction recipes for POSes.
    
    CCP Table: invTypeReactions
    CCP Primary key: ("reactionTypeID" smallint(6), "input" tinyint(1), "typeID" smallint(6))
    """
    INPUT_TYPES = ((0, 'Result of reaction'), 
                   (1, 'Reaction material'))
    
    reaction_type = models.ForeignKey(InvType,
                    related_name='inventorytypereactions_reaction_type_set')
    input = models.IntegerField(choices=INPUT_TYPES, blank=True, null=True)
    type = models.ForeignKey(InvType,
                    related_name='inventorytypereactions_type_set', 
                    help_text="Reaction result or material.")
    quantity = models.IntegerField(blank=True, null=True)
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Inventory Type Reaction'
        verbose_name_plural = 'Inventory Type Reactions'
        unique_together = ('reaction_type', 'input', 'type')
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class InvContrabandType(models.Model):
    """
    Points to an InventoryType that is considered contraband somewhere.
    
    CCP Table: invContrabandTypes
    CCP Primary key: ("factionID" int(11), "typeID" smallint(6))
    """
    faction = models.ForeignKey('ChrFaction')
    type = models.ForeignKey(InvType)
    standing_loss = models.FloatField(blank=True, null=True)
    confiscate_min_sec = models.FloatField(blank=True, null=True)
    fine_by_value = models.FloatField(blank=True, null=True)
    attack_min_sec = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Contraband'
        verbose_name_plural = 'Contraband'
        unique_together = ('faction', 'type')

    def __unicode__(self):
        return self.type

    def __str__(self):
        return self.__unicode__()
