"""
Admin interface models. Automatically detected by admin.autodiscover().
"""
from django.contrib import admin
from eve_db.models import *

class InvCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_published')
admin.site.register(InvCategory, InvCategoryAdmin)

class ChrBloodlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'race', 'corporation')
admin.site.register(ChrBloodline, ChrBloodlineAdmin)

class ChrAncestryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bloodline', 'short_description')
admin.site.register(ChrAncestry, ChrAncestryAdmin)

class ChrAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'short_description')
    list_display_links = ('id', 'name')
admin.site.register(ChrAttribute, ChrAttributeAdmin)

class InvNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(InvName, InvNameAdmin)

class InvMetaGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon')
admin.site.register(InvMetaGroup, InvMetaGroupAdmin)

class InvMetaTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'parent_type', 'meta_group')
admin.site.register(InvMetaType, InvMetaTypeAdmin)

class InvGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(InvGroup, InvGroupAdmin)

class InvTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'market_group', 'description')
admin.site.register(InvType, InvTypeAdmin)

class InvFlagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'type_text', 'order')
admin.site.register(InvFlag, InvFlagAdmin)

class DgmEffectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'is_offensive',
                    'is_assistance', 'is_published')
admin.site.register(DgmEffect, DgmEffectAdmin)

class DgmTypeEffectAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'effect', 'is_default')
admin.site.register(DgmTypeEffect, DgmTypeEffectAdmin)

class InvTypeReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'reaction_type', 'type', 'input')
admin.site.register(InvTypeReaction, InvTypeReactionAdmin)

class InvPOSResourcePurposeAdmin(admin.ModelAdmin):
    list_display = ('id', 'purpose')
admin.site.register(InvPOSResourcePurpose, InvPOSResourcePurposeAdmin)

class InvPOSResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'control_tower_type', 'resource_type', 'purpose',
                    'quantity', 'faction')
admin.site.register(InvPOSResource, InvPOSResourceAdmin)

class InvContrabandTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'faction', 'standing_loss',
                    'confiscate_min_sec', 'attack_min_sec', 'fine_by_value')
admin.site.register(InvContrabandType, InvContrabandTypeAdmin)

class InvBlueprintTypeAdmin(admin.ModelAdmin):
    list_display = ('blueprint_type', 'product_type', 'tech_level')
admin.site.register(InvBlueprintType, InvBlueprintTypeAdmin)

class RamActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon_filename', 'is_published')
admin.site.register(RamActivity, RamActivityAdmin)

class RamAssemblyLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'station', 'owner', 'activity',
                    'minimum_char_security', 'cost_per_hour')
admin.site.register(RamAssemblyLine, RamAssemblyLineAdmin)

class RamAssemblyLineStationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'station', 'assembly_line_type', 'quantity',
                    'station_type', 'owner', 'solar_system', 'region')
admin.site.register(RamAssemblyLineStations, RamAssemblyLineStationsAdmin)

class RamAssemblyLineTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'base_time_multiplier',
                    'base_material_multiplier', 'activity',
                    'min_cost_per_hour')
admin.site.register(RamAssemblyLineType, RamAssemblyLineTypeAdmin)

class RamAssemblyLineTypeDetailPerCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'assembly_line_type', 'category',
                    'time_multiplier', 'material_multiplier')
admin.site.register(RamAssemblyLineTypeDetailPerCategory,
                    RamAssemblyLineTypeDetailPerCategoryAdmin)

class RamAssemblyLineTypeDetailPerGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'assembly_line_type', 'group',
                    'time_multiplier', 'material_multiplier')
admin.site.register(RamAssemblyLineTypeDetailPerGroup,
                    RamAssemblyLineTypeDetailPerGroupAdmin)

class EveUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name', 'description')
admin.site.register(EveUnit, EveUnitAdmin)

class MapUniverseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(MapUniverse, MapUniverseAdmin)

class MapRegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction')
admin.site.register(MapRegion, MapRegionAdmin)

class MapRegionJumpAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_region', 'to_region')
admin.site.register(MapRegionJump, MapRegionJumpAdmin)

class MapConstellationJumpAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_constellation', 'from_region',
                    'to_constellation', 'to_region')
admin.site.register(MapConstellationJump, MapConstellationJumpAdmin)

class ChrFactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'solar_system')
admin.site.register(ChrFaction, ChrFactionAdmin)

class MapConstellationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction')
admin.site.register(MapConstellation, MapConstellationAdmin)

class MapSolarSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'constellation', 'region', 'faction',
                    'security_class', 'security_level')
admin.site.register(MapSolarSystem, MapSolarSystemAdmin)

class MapSolarSystemJumpAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_solar_system', 'from_constellation',
                    'from_region', 'to_solar_system', 'to_constellation',
                    'to_region')
admin.site.register(MapSolarSystemJump, MapSolarSystemJumpAdmin)

class MapJumpAdmin(admin.ModelAdmin):
    list_display = ('origin_gate', 'destination_gate')
admin.site.register(MapJump, MapJumpAdmin)

class DgmAttributeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(DgmAttributeCategory, DgmAttributeCategoryAdmin)

class DgmAttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(DgmAttributeType, DgmAttributeTypeAdmin)

class DgmTypeAttributeAdmin(admin.ModelAdmin):
    list_display = ('inventory_type', 'attribute', 'value_int', 'value_float')
admin.site.register(DgmTypeAttribute, DgmTypeAttributeAdmin)

class EveGraphicAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'name', 'file', 'is_obsolete')
admin.site.register(EveGraphic, EveGraphicAdmin)

class ChrRaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description')
admin.site.register(ChrRace, ChrRaceAdmin)

class CrpActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(CrpActivity, CrpActivityAdmin)

class CrpNPCCorporationDivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'corporation', 'division', 'size')
admin.site.register(CrpNPCCorporationDivision, CrpNPCCorporationDivisionAdmin)

class CrpNPCCorporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction', 'description', 'station_count',
                    'size', 'extent')
admin.site.register(CrpNPCCorporation, CrpNPCCorporationAdmin)

class CrpNPCCorporationTradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'corporation', 'type')
admin.site.register(CrpNPCCorporationTrade, CrpNPCCorporationTradeAdmin)

class CrpNPCCorporationResearchFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'corporation', 'skill')
admin.site.register(CrpNPCCorporationResearchField,
                    CrpNPCCorporationResearchFieldAdmin)

class CrpNPCDivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'leader_type')
admin.site.register(CrpNPCDivision, CrpNPCDivisionAdmin)

class StaOperationServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'operation', 'service')
admin.site.register(StaOperationServices, StaOperationServicesAdmin)

class StaServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(StaService, StaServiceAdmin)

class StaStationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'dock_entry_x', 'dock_orientation_x', 'dock_entry_y',
                    'dock_orientation_y', 'dock_entry_z', 'dock_orientation_z',
                    'operation', 'office_slots', 'reprocessing_efficiency',
                    'is_conquerable')
admin.site.register(StaStationType, StaStationTypeAdmin)

class StaOperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity_id', 'name', 'description',
                    'fringe', 'corridor', 'hub', 'border', 'ratio')
admin.site.register(StaOperation, StaOperationAdmin)

class MapDenormalizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'group', 'constellation', 'region',
                    'orbit_id', 'x', 'y', 'z', 'radius', 'name',
                    'security', 'celestial_index', 'orbit_index')
admin.site.register(MapDenormalize, MapDenormalizeAdmin)

class MapCelestialStatisticAdmin(admin.ModelAdmin):
    list_display = ('celestial',)
admin.site.register(MapCelestialStatistic, MapCelestialStatisticAdmin)

class MapLandmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'solar_system',
                    'importance', 'radius')
admin.site.register(MapLandmark, MapLandmarkAdmin)

class StaStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'security',
                    'office_rental_cost',
                    'operation', 'type', 'corporation',
                    'solar_system', 'constellation', 'region')
admin.site.register(StaStation, StaStationAdmin)

class AgtAgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'division', 'corporation', 'location',
                    'quality', 'level')
admin.site.register(AgtAgent, AgtAgentAdmin)

class AgtAgentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(AgtAgentType, AgtAgentTypeAdmin)

class AgtConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'agent', 'key', 'value')
admin.site.register(AgtConfig, AgtConfigAdmin)

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

class PlanetSchematicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cycle_time')
admin.site.register(PlanetSchematic, PlanetSchematicAdmin)

class PlanetSchematicsPinMapAdmin(admin.ModelAdmin):
    list_display = ('id', 'schematic', 'type')
admin.site.register(PlanetSchematicsPinMap, PlanetSchematicsPinMapAdmin)

class PlanetSchematicsTypeMapAdmin(admin.ModelAdmin):
    list_display = ('id', 'schematic', 'type', 'quantity', 'is_input')
admin.site.register(PlanetSchematicsTypeMap, PlanetSchematicsTypeMapAdmin)
