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

class EVECharAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'short_description')
    list_display_links = ('id', 'name')
admin.site.register(EVECharAttribute, EVECharAttributeAdmin)

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

class EVERamActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon_filename', 'is_published')
admin.site.register(EVERamActivity, EVERamActivityAdmin)

class EVERamAssemblyLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'station', 'owner', 'activity',
                    'minimum_char_security', 'cost_per_hour')
admin.site.register(EVERamAssemblyLine, EVERamAssemblyLineAdmin)

class EVERamAssemblyLineStationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'station', 'assembly_line_type', 'quantity',
                    'station_type', 'owner', 'solar_system', 'region')
admin.site.register(EVERamAssemblyLineStations, EVERamAssemblyLineStationsAdmin)

class EVERamAssemblyLineTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'base_time_multiplier',
                    'base_material_multiplier', 'activity',
                    'min_cost_per_hour')
admin.site.register(EVERamAssemblyLineType, EVERamAssemblyLineTypeAdmin)

class EVERamAssemblyLineTypeDetailPerCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'assembly_line_type', 'category',
                    'time_multiplier', 'material_multiplier')
admin.site.register(EVERamAssemblyLineTypeDetailPerCategory,
                    EVERamAssemblyLineTypeDetailPerCategoryAdmin)

class EVERamAssemblyLineTypeDetailPerGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'assembly_line_type', 'group',
                    'time_multiplier', 'material_multiplier')
admin.site.register(EVERamAssemblyLineTypeDetailPerGroup,
                    EVERamAssemblyLineTypeDetailPerGroupAdmin)
 
class EVEUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name', 'description')
admin.site.register(EVEUnit, EVEUnitAdmin)

class EVEUniverseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(EVEUniverse, EVEUniverseAdmin)

class EVERegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction')
admin.site.register(EVERegion, EVERegionAdmin)

class EVERegionJumpAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_region', 'to_region')
admin.site.register(EVERegionJump, EVERegionJumpAdmin)

class EVEConstellationJumpAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_constellation', 'from_region', 
                    'to_constellation', 'to_region')
admin.site.register(EVEConstellationJump, EVEConstellationJumpAdmin)

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

class EVESolarSystemJumpAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_solar_system', 'from_constellation', 
                    'from_region', 'to_solar_system', 'to_constellation', 
                    'to_region')
admin.site.register(EVESolarSystemJump, EVESolarSystemJumpAdmin)

class EVEStargateJumpAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin_gate', 'destination_gate')
admin.site.register(EVEStargateJump, EVEStargateJumpAdmin)
 
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

class EVENPCCorporationDivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'corporation', 'division', 'size')
admin.site.register(EVENPCCorporationDivision, EVENPCCorporationDivisionAdmin)

class EVENPCCorporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction', 'description', 'station_count', 
                    'size', 'extent')
admin.site.register(EVENPCCorporation, EVENPCCorporationAdmin)

class EVENPCCorporationTradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'corporation', 'type')
admin.site.register(EVENPCCorporationTrade, EVENPCCorporationTradeAdmin)

class EVENPCCorporationResearchFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'corporation', 'skill')
admin.site.register(EVENPCCorporationResearchField,
                    EVENPCCorporationResearchFieldAdmin)

class EVENPCDivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'leader_type')
admin.site.register(EVENPCDivision, EVENPCDivisionAdmin)

class EVEStationOperationServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'operation', 'service')
admin.site.register(EVEStationOperationServices, EVEStationOperationServicesAdmin)

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
    list_display = ('id', 'activity_id', 'name', 'description',
                    'fringe', 'corridor', 'hub', 'border', 'ratio')
admin.site.register(EVEStationOperation, EVEStationOperationAdmin)
 
class EVEMapDenormalizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'group', 'constellation', 'region',
                    'orbit_id', 'x', 'y', 'z', 'radius', 'name',
                    'security', 'celestial_index', 'orbit_index')
admin.site.register(EVEMapDenormalize, EVEMapDenormalizeAdmin)

class EVECelestialStatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'celestial')
admin.site.register(EVECelestialStatistic, EVECelestialStatisticAdmin)

class EVELandmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'solar_system',
                    'importance', 'radius')
admin.site.register(EVELandmark, EVELandmarkAdmin)

class EVEStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'security',
                    'office_rental_cost',
                    'operation', 'type', 'corporation',
                    'solar_system', 'constellation', 'region')
admin.site.register(EVEStation, EVEStationAdmin)

class EVEAgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'division', 'corporation', 'location',
                    'quality', 'level') 
admin.site.register(EVEAgent, EVEAgentAdmin)

class EVEAgentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(EVEAgentType, EVEAgentTypeAdmin)

class EVEAgentConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'agent', 'key', 'value')
admin.site.register(EVEAgentConfig, EVEAgentConfigAdmin)

class CrtCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(CrtCategory, CrtCategoryAdmin)

class CrtClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(CrtClass, CrtClassAdmin)

class CrtCertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'cert_class', 'grade', 'corporation',
                    'icon_num', 'description')
admin.site.register(CrtCertificate, CrtCertificateAdmin)

class CrtRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'parent_type', 'parent_level', 'child')
admin.site.register(CrtRelationship, CrtRelationshipAdmin)

class CrtRecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'ship_type', 'certificate', 'recommendation_level')
admin.site.register(CrtRecommendation, CrtRecommendationAdmin)