"""
Admin interface models. Automatically detected by admin.autodiscover().
"""
from django.contrib import admin
from eve_db.models import *

class EVEInventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_published')
admin.site.register(EVEInventoryCategory, EVEInventoryCategoryAdmin)

class EVEBloodlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'race', 'corporation')
admin.site.register(EVEBloodline, EVEBloodlineAdmin)

class EVEAncestryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bloodline', 'short_description')
admin.site.register(EVEAncestry, EVEAncestryAdmin)

class EVEInventoryMetaGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'graphic')
admin.site.register(EVEInventoryMetaGroup, EVEInventoryMetaGroupAdmin)

class EVEInventoryMetaTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'parent_type', 'meta_group')
admin.site.register(EVEInventoryMetaType, EVEInventoryMetaTypeAdmin)

class EVEInventoryGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(EVEInventoryGroup, EVEInventoryGroupAdmin)

class EVEInventoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'market_group', 'description')
admin.site.register(EVEInventoryType, EVEInventoryTypeAdmin)

class EVEInventoryFlagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'type_text', 'order')
admin.site.register(EVEInventoryFlag, EVEInventoryFlagAdmin)

class EVEInventoryEffectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'is_offensive',
                    'is_assistance', 'is_published')
admin.site.register(EVEInventoryEffect, EVEInventoryEffectAdmin)

class EVEInventoryTypeEffectAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'effect', 'is_default')
admin.site.register(EVEInventoryTypeEffect, EVEInventoryTypeEffectAdmin)

class EVEInventoryTypeReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'reaction_type', 'type', 'input')
admin.site.register(EVEInventoryTypeReaction, EVEInventoryTypeReactionAdmin)

class EVEPOSResourcePurposeAdmin(admin.ModelAdmin):
    list_display = ('id', 'purpose')
admin.site.register(EVEPOSResourcePurpose, EVEPOSResourcePurposeAdmin)

class EVEPOSResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'control_tower_type', 'resource_type', 'purpose',
                    'quantity', 'faction')
admin.site.register(EVEPOSResource, EVEPOSResourceAdmin)

class EVEContrabandTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'faction', 'standing_loss', 
                    'confiscate_min_sec', 'attack_min_sec', 'fine_by_value')
admin.site.register(EVEContrabandType, EVEContrabandTypeAdmin)

class EVEInventoryBlueprintTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'blueprint_type', 'product_type', 'tech_level')
admin.site.register(EVEInventoryBlueprintType, EVEInventoryBlueprintTypeAdmin)

class EVEResearchAndMfgActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon_filename', 'is_published')
admin.site.register(EVEResearchAndMfgActivity, EVEResearchAndMfgActivityAdmin)
 
class EVEUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name', 'description')
admin.site.register(EVEUnit, EVEUnitAdmin)

class EVEUniverseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(EVEUniverse, EVEUniverseAdmin)

class EVERegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction')
admin.site.register(EVERegion, EVERegionAdmin)

class EVEFactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'solar_system')
admin.site.register(EVEFaction, EVEFactionAdmin)

class EVEConstellationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction', 'alliance')
admin.site.register(EVEConstellation, EVEConstellationAdmin)

class EVESolarSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'constellation', 'region', 'faction', 
                    'alliance', 'security_class', 'security_level')
admin.site.register(EVESolarSystem, EVESolarSystemAdmin)
 
class EVEInventoryAttributeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(EVEInventoryAttributeCategory, EVEInventoryAttributeCategoryAdmin)
 
class EVEInventoryAttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(EVEInventoryAttributeType, EVEInventoryAttributeTypeAdmin)
 
class EVEInventoryTypeAttributeAdmin(admin.ModelAdmin):
    list_display = ('inventory_type', 'attribute', 'value_int', 'value_float')
admin.site.register(EVEInventoryTypeAttribute, EVEInventoryTypeAttributeAdmin)

class EVEGraphicAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'name', 'icon_filename')
admin.site.register(EVEGraphic, EVEGraphicAdmin)

class EVEInventoryNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'group', 'type')
admin.site.register(EVEInventoryName, EVEInventoryNameAdmin)

class EVERaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description')
admin.site.register(EVERace, EVERaceAdmin)

class EVECorporateActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(EVECorporateActivity, EVECorporateActivityAdmin)

class EVENPCCorporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction', 'description', 'station_count', 
                    'size', 'extent')
admin.site.register(EVENPCCorporation, EVENPCCorporationAdmin)

class EVENPCCorporationDivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'leader_type')
admin.site.register(EVENPCCorporationDivision, EVENPCCorporationDivisionAdmin)

class EVEStationServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(EVEStationService, EVEStationServiceAdmin)

class EVEStationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'docking_bay_graphic', 'hangar_graphic',
                    'dock_entry_x', 'dock_orientation_x', 'dock_entry_y',
                    'dock_orientation_y', 'dock_entry_z', 'dock_orientation_z',
                    'operation', 'office_slots', 'reprocessing_efficiency', 'is_conquerable')
admin.site.register(EVEStationType, EVEStationTypeAdmin)
 
class EVEStationOperationAdmin(admin.ModelAdmin):
    """
    Unsolved issue when any of these are added to the admin panel:
    'caldari_station_type', 'minmatar_station_type'
    'amarr_station_type', 'gallente_station_type',
    'jove_station_type'
    
    "Caught an exception while rendering: 'EVEStationType'
    object has no attribute 'name'"
    """
     
    list_display = ('id', 'activity_id', 'name', 'description',
                    'fringe', 'corridor', 'hub', 'border', 'ratio')
admin.site.register(EVEStationOperation, EVEStationOperationAdmin)
 
class EVEMapDenormalizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'group', 'constellation', 'region',
                    'orbit_id', 'x', 'y', 'z', 'radius', 'name',
                    'security', 'celestial_index', 'orbit_index')
admin.site.register(EVEMapDenormalize, EVEMapDenormalizeAdmin)

class EVEStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'security',
                    'office_rental_cost',
                    'operation', 'type', 'corporation',
                    'solar_system', 'constellation', 'region')
admin.site.register(EVEStation, EVEStationAdmin)
