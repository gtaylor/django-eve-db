# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EveName'
        db.create_table('eve_db_evename', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvCategory'], null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvGroup'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['EveName'])

        # Adding model 'EVEUnit'
        db.create_table('eve_db_eveunit', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('eve_db', ['EVEUnit'])

        # Adding model 'EVEGraphic'
        db.create_table('eve_db_evegraphic', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('icon_filename', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('is_obsolete', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('eve_db', ['EVEGraphic'])

        # Adding model 'InvMarketGroup'
        db.create_table('eve_db_invmarketgroup', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvMarketGroup'], null=True, blank=True)),
            ('has_items', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvMarketGroup'])

        # Adding model 'InvCategory'
        db.create_table('eve_db_invcategory', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvCategory'])

        # Adding model 'InvGroup'
        db.create_table('eve_db_invgroup', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvCategory'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
            ('use_base_price', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('allow_manufacture', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('allow_recycle', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('allow_anchoring', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_anchored', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_fittable_non_singleton', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvGroup'])

        # Adding model 'InvMetaGroup'
        db.create_table('eve_db_invmetagroup', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvMetaGroup'])

        # Adding model 'InvType'
        db.create_table('eve_db_invtype', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvGroup'], null=True, blank=True)),
            ('market_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvMarketGroup'], null=True, blank=True)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
            ('radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mass', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('capacity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('portion_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.ChrRace'], null=True, blank=True)),
            ('base_price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('chance_of_duplicating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvType'])

        # Adding model 'InvTypeMaterial'
        db.create_table('eve_db_invtypematerial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='material_set', to=orm['eve_db.InvType'])),
            ('material_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemtype_set', to=orm['eve_db.InvType'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('eve_db', ['InvTypeMaterial'])

        # Adding unique constraint on 'InvTypeMaterial', fields ['type', 'material_type']
        db.create_unique('eve_db_invtypematerial', ['type_id', 'material_type_id'])

        # Adding model 'InvMetaType'
        db.create_table('eve_db_invmetatype', (
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventorymetatype_type_set', unique=True, primary_key=True, to=orm['eve_db.InvType'])),
            ('parent_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventorymetatype_parent_type_set', to=orm['eve_db.InvType'])),
            ('meta_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvMetaGroup'])),
        ))
        db.send_create_signal('eve_db', ['InvMetaType'])

        # Adding model 'InvFlag'
        db.create_table('eve_db_invflag', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('type_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvFlag'])

        # Adding model 'DgmAttributeCategory'
        db.create_table('eve_db_dgmattributecategory', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('eve_db', ['DgmAttributeCategory'])

        # Adding model 'DgmAttributeType'
        db.create_table('eve_db_dgmattributetype', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.DgmAttributeCategory'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
            ('defaultvalue', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEUnit'], null=True, blank=True)),
            ('is_stackable', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('high_is_good', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['DgmAttributeType'])

        # Adding model 'DgmTypeAttribute'
        db.create_table('eve_db_dgmtypeattribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inventory_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.DgmAttributeType'])),
            ('value_int', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('value_float', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['DgmTypeAttribute'])

        # Adding unique constraint on 'DgmTypeAttribute', fields ['inventory_type', 'attribute']
        db.create_unique('eve_db_dgmtypeattribute', ['inventory_type_id', 'attribute_id'])

        # Adding model 'InvBlueprintType'
        db.create_table('eve_db_invblueprinttype', (
            ('blueprint_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blueprint_type_set', unique=True, primary_key=True, to=orm['eve_db.InvType'])),
            ('product_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blueprint_product_type_set', to=orm['eve_db.InvType'])),
            ('parent_blueprint_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parent_blueprint_type_set', null=True, to=orm['eve_db.InvType'])),
            ('tech_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('research_productivity_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('research_material_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('research_copy_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('research_tech_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('productivity_modifier', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('material_modifier', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('waste_factor', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max_production_limit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvBlueprintType'])

        # Adding model 'DgmEffect'
        db.create_table('eve_db_dgmeffect', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('category', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pre_expression', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('post_expression', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
            ('is_offensive', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_assistance', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('duration_attribute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inventoryeffectdurationeattribute', null=True, to=orm['eve_db.DgmAttributeType'])),
            ('tracking_speed_attribute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inventoryeffecttrackingspeedattribute', null=True, to=orm['eve_db.DgmAttributeType'])),
            ('discharge_attribute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inventoryeffectdischargeattribute', null=True, to=orm['eve_db.DgmAttributeType'])),
            ('range_attribute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inventoryeffectrangeattribute', null=True, to=orm['eve_db.DgmAttributeType'])),
            ('falloff_attribute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inventoryeffectfalloffattribute', null=True, to=orm['eve_db.DgmAttributeType'])),
            ('disallow_auto_repeat', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('is_warp_safe', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('has_range_chance', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('has_electronic_chance', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('has_propulsion_chance', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('distribution', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sfx_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('npc_usage_chance_attribute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inventoryeffectnpcusagechanceattribute', null=True, to=orm['eve_db.DgmAttributeType'])),
            ('npc_activation_chance_attribute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inventoryeffectnpcactivationchanceattribute', null=True, to=orm['eve_db.DgmAttributeType'])),
            ('fitting_usage_chance_attribute', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inventoryeffectfittingusagechanceattribute', null=True, to=orm['eve_db.DgmAttributeType'])),
        ))
        db.send_create_signal('eve_db', ['DgmEffect'])

        # Adding model 'DgmTypeEffect'
        db.create_table('eve_db_dgmtypeeffect', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'])),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.DgmEffect'])),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('eve_db', ['DgmTypeEffect'])

        # Adding unique constraint on 'DgmTypeEffect', fields ['type', 'effect']
        db.create_unique('eve_db_dgmtypeeffect', ['type_id', 'effect_id'])

        # Adding model 'InvPOSResourcePurpose'
        db.create_table('eve_db_invposresourcepurpose', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvPOSResourcePurpose'])

        # Adding model 'InvPOSResource'
        db.create_table('eve_db_invposresource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('control_tower_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tower_resource_set', to=orm['eve_db.InvType'])),
            ('resource_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pos_resource_set', to=orm['eve_db.InvType'])),
            ('purpose', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvPOSResourcePurpose'], null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('min_security_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.ChrFaction'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvPOSResource'])

        # Adding unique constraint on 'InvPOSResource', fields ['control_tower_type', 'resource_type']
        db.create_unique('eve_db_invposresource', ['control_tower_type_id', 'resource_type_id'])

        # Adding model 'InvTypeReaction'
        db.create_table('eve_db_invtypereaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reaction_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventorytypereactions_reaction_type_set', to=orm['eve_db.InvType'])),
            ('input', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inventorytypereactions_type_set', to=orm['eve_db.InvType'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvTypeReaction'])

        # Adding unique constraint on 'InvTypeReaction', fields ['reaction_type', 'input', 'type']
        db.create_unique('eve_db_invtypereaction', ['reaction_type_id', 'input', 'type_id'])

        # Adding model 'InvContrabandType'
        db.create_table('eve_db_invcontrabandtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.ChrFaction'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'])),
            ('standing_loss', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('confiscate_min_sec', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('fine_by_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('attack_min_sec', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['InvContrabandType'])

        # Adding unique constraint on 'InvContrabandType', fields ['faction', 'type']
        db.create_unique('eve_db_invcontrabandtype', ['faction_id', 'type_id'])

        # Adding model 'MapUniverse'
        db.create_table('eve_db_mapuniverse', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('x_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['MapUniverse'])

        # Adding model 'MapRegion'
        db.create_table('eve_db_mapregion', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.ChrFaction'], null=True, blank=True)),
            ('x_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['MapRegion'])

        # Adding model 'MapRegionJump'
        db.create_table('eve_db_mapregionjump', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_region', self.gf('django.db.models.fields.related.ForeignKey')(related_name='region_jumps_from_region_set', to=orm['eve_db.MapRegion'])),
            ('to_region', self.gf('django.db.models.fields.related.ForeignKey')(related_name='region_jumps_to_region_set', to=orm['eve_db.MapRegion'])),
        ))
        db.send_create_signal('eve_db', ['MapRegionJump'])

        # Adding unique constraint on 'MapRegionJump', fields ['from_region', 'to_region']
        db.create_unique('eve_db_mapregionjump', ['from_region_id', 'to_region_id'])

        # Adding model 'MapConstellation'
        db.create_table('eve_db_mapconstellation', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapRegion'], null=True, blank=True)),
            ('x_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alliance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_api.ApiPlayerAlliance'], null=True, blank=True)),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.ChrFaction'], null=True, blank=True)),
            ('sovereignty_start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sovereignty_grace_start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['MapConstellation'])

        # Adding model 'MapConstellationJump'
        db.create_table('eve_db_mapconstellationjump', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_region', self.gf('django.db.models.fields.related.ForeignKey')(related_name='constellation_jumps_from_region_set', to=orm['eve_db.MapRegion'])),
            ('from_constellation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='constellation_jumps_from_constellation_set', to=orm['eve_db.MapConstellation'])),
            ('to_region', self.gf('django.db.models.fields.related.ForeignKey')(related_name='constellation_jumps_to_region_set', to=orm['eve_db.MapRegion'])),
            ('to_constellation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='constellation_jumps_to_constellation_set', to=orm['eve_db.MapConstellation'])),
        ))
        db.send_create_signal('eve_db', ['MapConstellationJump'])

        # Adding unique constraint on 'MapConstellationJump', fields ['from_constellation', 'to_constellation']
        db.create_unique('eve_db_mapconstellationjump', ['from_constellation_id', 'to_constellation_id'])

        # Adding model 'MapSolarSystem'
        db.create_table('eve_db_mapsolarsystem', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapRegion'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('constellation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapConstellation'], null=True, blank=True)),
            ('x_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('luminosity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('is_border_system', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_fringe_system', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_corridor_system', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_hub_system', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_international', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('has_interregional_link', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('has_interconstellational_link', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('security_level', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='solarsystem_set', null=True, to=orm['eve_db.ChrFaction'])),
            ('radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('sun_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'], null=True, blank=True)),
            ('security_class', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('alliance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_api.ApiPlayerAlliance'], null=True, blank=True)),
            ('sovereignty_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sovereignty_start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['MapSolarSystem'])

        # Adding model 'MapSolarSystemJump'
        db.create_table('eve_db_mapsolarsystemjump', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_region', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='solar_system_jumps_from_region_set', null=True, to=orm['eve_db.MapRegion'])),
            ('from_constellation', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='solar_system_jumps_from_constellation_set', null=True, to=orm['eve_db.MapConstellation'])),
            ('from_solar_system', self.gf('django.db.models.fields.related.ForeignKey')(related_name='solar_system_jumps_from_solar_system_set', to=orm['eve_db.MapSolarSystem'])),
            ('to_region', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='solar_system_jumps_to_region_set', null=True, to=orm['eve_db.MapRegion'])),
            ('to_constellation', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='solar_system_jumps_to_constellation_set', null=True, to=orm['eve_db.MapConstellation'])),
            ('to_solar_system', self.gf('django.db.models.fields.related.ForeignKey')(related_name='solar_system_jumps_to_solar_system_set', to=orm['eve_db.MapSolarSystem'])),
        ))
        db.send_create_signal('eve_db', ['MapSolarSystemJump'])

        # Adding unique constraint on 'MapSolarSystemJump', fields ['from_solar_system', 'to_solar_system']
        db.create_unique('eve_db_mapsolarsystemjump', ['from_solar_system_id', 'to_solar_system_id'])

        # Adding model 'MapJump'
        db.create_table('eve_db_mapjump', (
            ('origin_gate', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stargate_jump_origin_set', unique=True, primary_key=True, to=orm['eve_db.MapDenormalize'])),
            ('destination_gate', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stargate_jump_destination_set', to=orm['eve_db.MapDenormalize'])),
        ))
        db.send_create_signal('eve_db', ['MapJump'])

        # Adding model 'MapCelestialStatistic'
        db.create_table('eve_db_mapcelestialstatistic', (
            ('celestial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapDenormalize'], unique=True, primary_key=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('spectral_class', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('luminousity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('life', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('orbit_radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('eccentricity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mass_dust', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mass_gas', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('is_fragmented', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('density', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('surface_gravity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('escape_velocity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('orbit_period', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rotation_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('is_locked', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pressure', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mass', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['MapCelestialStatistic'])

        # Adding model 'MapDenormalize'
        db.create_table('eve_db_mapdenormalize', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'], null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvGroup'], null=True, blank=True)),
            ('solar_system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapSolarSystem'], null=True, blank=True)),
            ('constellation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapConstellation'], null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapRegion'], null=True, blank=True)),
            ('orbit_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('security', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('celestial_index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('orbit_index', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['MapDenormalize'])

        # Adding model 'MapLandmark'
        db.create_table('eve_db_maplandmark', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('solar_system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapSolarSystem'], null=True, blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('radius', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
            ('importance', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('url_2d', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('eve_db', ['MapLandmark'])

        # Adding model 'ChrRace'
        db.create_table('eve_db_chrrace', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('short_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['ChrRace'])

        # Adding model 'ChrBloodline'
        db.create_table('eve_db_chrbloodline', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='bloodline_set', null=True, to=orm['eve_db.ChrRace'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('male_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('female_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('starter_ship_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='bloodline_starter_ship_set', null=True, to=orm['eve_db.InvType'])),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'], null=True, blank=True)),
            ('starting_perception', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('starting_willpower', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('starting_charisma', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('starting_memory', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('starting_intelligence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('short_male_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('short_female_description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('eve_db', ['ChrBloodline'])

        # Adding model 'ChrAncestry'
        db.create_table('eve_db_chrancestry', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('bloodline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.ChrBloodline'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('perception_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('willpower_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('charisma_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('memory_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intelligence_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('eve_db', ['ChrAncestry'])

        # Adding model 'ChrAttribute'
        db.create_table('eve_db_chrattribute', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('graphic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.EVEGraphic'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['ChrAttribute'])

        # Adding model 'ChrFaction'
        db.create_table('eve_db_chrfaction', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('solar_system', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='faction_set', null=True, to=orm['eve_db.MapSolarSystem'])),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='faction_set', null=True, to=orm['eve_db.CrpNPCCorporation'])),
            ('size_factor', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('station_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('station_system_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('eve_db', ['ChrFaction'])

        # Adding model 'CrpActivity'
        db.create_table('eve_db_crpactivity', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrpActivity'])

        # Adding model 'CrpNPCCorporation'
        db.create_table('eve_db_crpnpccorporation', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('extent', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('solar_system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapSolarSystem'], null=True, blank=True)),
            ('investor1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='invested1_set', null=True, to=orm['eve_db.CrpNPCCorporation'])),
            ('investor1_shares', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('investor2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='invested2_set', null=True, to=orm['eve_db.CrpNPCCorporation'])),
            ('investor2_shares', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('investor3', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='invested3_set', null=True, to=orm['eve_db.CrpNPCCorporation'])),
            ('investor3_shares', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('investor4', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='invested4_set', null=True, to=orm['eve_db.CrpNPCCorporation'])),
            ('investor4_shares', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('friendly_corp', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='friendly_with_set', null=True, to=orm['eve_db.CrpNPCCorporation'])),
            ('enemy_corp', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='enemy_of_set', null=True, to=orm['eve_db.CrpNPCCorporation'])),
            ('public_share_percent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('initial_share_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('min_security', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('stations_are_scattered', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('fringe_systems', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('corridor_systems', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hub_systems', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('border_systems', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.ChrFaction'], null=True, blank=True)),
            ('size_factor', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('station_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('station_system_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('eve_db', ['CrpNPCCorporation'])

        # Adding model 'CrpNPCDivision'
        db.create_table('eve_db_crpnpcdivision', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('leader_type', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrpNPCDivision'])

        # Adding model 'CrpNPCCorporationDivision'
        db.create_table('eve_db_crpnpccorporationdivision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'])),
            ('division', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCDivision'])),
            ('size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrpNPCCorporationDivision'])

        # Adding unique constraint on 'CrpNPCCorporationDivision', fields ['corporation', 'division']
        db.create_unique('eve_db_crpnpccorporationdivision', ['corporation_id', 'division_id'])

        # Adding model 'CrpNPCCorporationTrade'
        db.create_table('eve_db_crpnpccorporationtrade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrpNPCCorporationTrade'])

        # Adding unique constraint on 'CrpNPCCorporationTrade', fields ['corporation', 'type']
        db.create_unique('eve_db_crpnpccorporationtrade', ['corporation_id', 'type_id'])

        # Adding model 'CrpNPCCorporationResearchField'
        db.create_table('eve_db_crpnpccorporationresearchfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrpNPCCorporationResearchField'])

        # Adding unique constraint on 'CrpNPCCorporationResearchField', fields ['skill', 'corporation']
        db.create_unique('eve_db_crpnpccorporationresearchfield', ['skill_id', 'corporation_id'])

        # Adding model 'AgtAgentType'
        db.create_table('eve_db_agtagenttype', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('eve_db', ['AgtAgentType'])

        # Adding model 'AgtAgent'
        db.create_table('eve_db_agtagent', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('division', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCDivision'], null=True, blank=True)),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'], null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapDenormalize'], null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quality', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.AgtAgentType'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['AgtAgent'])

        # Adding model 'AgtConfig'
        db.create_table('eve_db_agtconfig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.AgtAgent'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['AgtConfig'])

        # Adding unique constraint on 'AgtConfig', fields ['agent', 'key']
        db.create_unique('eve_db_agtconfig', ['agent_id', 'key'])

        # Adding model 'RamActivity'
        db.create_table('eve_db_ramactivity', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('icon_filename', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['RamActivity'])

        # Adding model 'RamAssemblyLineType'
        db.create_table('eve_db_ramassemblylinetype', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('base_time_multiplier', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('base_material_multiplier', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.RamActivity'], null=True, blank=True)),
            ('min_cost_per_hour', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['RamAssemblyLineType'])

        # Adding model 'RamAssemblyLine'
        db.create_table('eve_db_ramassemblyline', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('assembly_line_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.RamAssemblyLineType'], null=True, blank=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.StaStation'], null=True, blank=True)),
            ('ui_grouping_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cost_install', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cost_per_hour', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('discount_per_good_standing_point', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('surcharge_per_bad_standing_point', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('minimum_standing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('minimum_char_security', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('minimum_corp_security', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('maximum_char_security', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('maximum_corp_security', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'], null=True, blank=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.RamActivity'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['RamAssemblyLine'])

        # Adding model 'RamAssemblyLineTypeDetailPerCategory'
        db.create_table('eve_db_ramassemblylinetypedetailpercategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assembly_line_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.RamAssemblyLineType'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvCategory'])),
            ('time_multiplier', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('material_multiplier', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['RamAssemblyLineTypeDetailPerCategory'])

        # Adding unique constraint on 'RamAssemblyLineTypeDetailPerCategory', fields ['assembly_line_type', 'category']
        db.create_unique('eve_db_ramassemblylinetypedetailpercategory', ['assembly_line_type_id', 'category_id'])

        # Adding model 'RamAssemblyLineTypeDetailPerGroup'
        db.create_table('eve_db_ramassemblylinetypedetailpergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assembly_line_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.RamAssemblyLineType'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvGroup'])),
            ('time_multiplier', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('material_multiplier', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['RamAssemblyLineTypeDetailPerGroup'])

        # Adding unique constraint on 'RamAssemblyLineTypeDetailPerGroup', fields ['assembly_line_type', 'group']
        db.create_unique('eve_db_ramassemblylinetypedetailpergroup', ['assembly_line_type_id', 'group_id'])

        # Adding model 'RamAssemblyLineStations'
        db.create_table('eve_db_ramassemblylinestations', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.StaStation'])),
            ('assembly_line_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.RamAssemblyLineType'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('station_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.StaStationType'], null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'], null=True, blank=True)),
            ('solar_system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapSolarSystem'], null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapRegion'], null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['RamAssemblyLineStations'])

        # Adding unique constraint on 'RamAssemblyLineStations', fields ['station', 'assembly_line_type']
        db.create_unique('eve_db_ramassemblylinestations', ['station_id', 'assembly_line_type_id'])

        # Adding model 'RamTypeRequirement'
        db.create_table('eve_db_ramtyperequirement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='type_requirement', to=orm['eve_db.InvType'])),
            ('activity_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.RamActivity'])),
            ('required_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='required_type', to=orm['eve_db.InvType'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('damage_per_job', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('recycle', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('eve_db', ['RamTypeRequirement'])

        # Adding unique constraint on 'RamTypeRequirement', fields ['type', 'activity_type', 'required_type']
        db.create_unique('eve_db_ramtyperequirement', ['type_id', 'activity_type_id', 'required_type_id'])

        # Adding model 'StaService'
        db.create_table('eve_db_staservice', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('eve_db', ['StaService'])

        # Adding model 'StaStationType'
        db.create_table('eve_db_stastationtype', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('docking_bay_graphic', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='docking_bay_graphic', null=True, to=orm['eve_db.EVEGraphic'])),
            ('hangar_graphic', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hangar_graphic', null=True, to=orm['eve_db.EVEGraphic'])),
            ('dock_entry_x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dock_orientation_x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dock_entry_y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dock_orientation_y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dock_entry_z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dock_orientation_z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.StaOperation'], null=True, blank=True)),
            ('office_slots', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('reprocessing_efficiency', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('is_conquerable', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('eve_db', ['StaStationType'])

        # Adding model 'StaOperation'
        db.create_table('eve_db_staoperation', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('activity_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fringe', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('corridor', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hub', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('border', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ratio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('caldari_station_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='caldari_station_operation_set', null=True, to=orm['eve_db.StaStationType'])),
            ('minmatar_station_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='minmatar_station_operation_set', null=True, to=orm['eve_db.StaStationType'])),
            ('amarr_station_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='amarr_station_operation_set', null=True, to=orm['eve_db.StaStationType'])),
            ('gallente_station_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='gallente_station_operation_set', null=True, to=orm['eve_db.StaStationType'])),
            ('jove_station_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='jove_station_operation_set', null=True, to=orm['eve_db.StaStationType'])),
        ))
        db.send_create_signal('eve_db', ['StaOperation'])

        # Adding model 'StaStation'
        db.create_table('eve_db_stastation', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('security', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('docking_cost_per_volume', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('max_ship_volume_dockable', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('office_rental_cost', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.StaOperation'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.StaStationType'], null=True, blank=True)),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'], null=True, blank=True)),
            ('solar_system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapSolarSystem'], null=True, blank=True)),
            ('constellation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapConstellation'], null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.MapRegion'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('z', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('reprocessing_efficiency', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('reprocessing_stations_take', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('reprocessing_hangar_flag', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['StaStation'])

        # Adding model 'StaOperationServices'
        db.create_table('eve_db_staoperationservices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.StaOperation'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.StaService'])),
        ))
        db.send_create_signal('eve_db', ['StaOperationServices'])

        # Adding unique constraint on 'StaOperationServices', fields ['operation', 'service']
        db.create_unique('eve_db_staoperationservices', ['operation_id', 'service_id'])

        # Adding model 'CrtCategory'
        db.create_table('eve_db_crtcategory', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrtCategory'])

        # Adding model 'CrtClass'
        db.create_table('eve_db_crtclass', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrtClass'])

        # Adding model 'CrtCertificate'
        db.create_table('eve_db_crtcertificate', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrtCategory'], null=True, blank=True)),
            ('cert_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrtClass'], null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrpNPCCorporation'], null=True, blank=True)),
            ('icon_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrtCertificate'])

        # Adding model 'CrtRelationship'
        db.create_table('eve_db_crtrelationship', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parent_crtrelationship_set', null=True, to=orm['eve_db.CrtCertificate'])),
            ('parent_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'], null=True, blank=True)),
            ('parent_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('child', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_crtrelationship_set', null=True, to=orm['eve_db.CrtCertificate'])),
        ))
        db.send_create_signal('eve_db', ['CrtRelationship'])

        # Adding model 'CrtRecommendation'
        db.create_table('eve_db_crtrecommendation', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('ship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'], null=True, blank=True)),
            ('certificate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.CrtCertificate'], null=True, blank=True)),
            ('recommendation_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['CrtRecommendation'])

        # Adding model 'PlanetSchematic'
        db.create_table('eve_db_planetschematic', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cycle_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eve_db', ['PlanetSchematic'])

        # Adding model 'PlanetSchematicsPinMap'
        db.create_table('eve_db_planetschematicspinmap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('schematic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.PlanetSchematic'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'])),
        ))
        db.send_create_signal('eve_db', ['PlanetSchematicsPinMap'])

        # Adding unique constraint on 'PlanetSchematicsPinMap', fields ['schematic', 'type']
        db.create_unique('eve_db_planetschematicspinmap', ['schematic_id', 'type_id'])

        # Adding model 'PlanetSchematicsTypeMap'
        db.create_table('eve_db_planetschematicstypemap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('schematic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.PlanetSchematic'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eve_db.InvType'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_input', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('eve_db', ['PlanetSchematicsTypeMap'])

        # Adding unique constraint on 'PlanetSchematicsTypeMap', fields ['schematic', 'type']
        db.create_unique('eve_db_planetschematicstypemap', ['schematic_id', 'type_id'])


    def backwards(self, orm):
        
        # Deleting model 'EveName'
        db.delete_table('eve_db_evename')

        # Deleting model 'EVEUnit'
        db.delete_table('eve_db_eveunit')

        # Deleting model 'EVEGraphic'
        db.delete_table('eve_db_evegraphic')

        # Deleting model 'InvMarketGroup'
        db.delete_table('eve_db_invmarketgroup')

        # Deleting model 'InvCategory'
        db.delete_table('eve_db_invcategory')

        # Deleting model 'InvGroup'
        db.delete_table('eve_db_invgroup')

        # Deleting model 'InvMetaGroup'
        db.delete_table('eve_db_invmetagroup')

        # Deleting model 'InvType'
        db.delete_table('eve_db_invtype')

        # Deleting model 'InvTypeMaterial'
        db.delete_table('eve_db_invtypematerial')

        # Removing unique constraint on 'InvTypeMaterial', fields ['type', 'material_type']
        db.delete_unique('eve_db_invtypematerial', ['type_id', 'material_type_id'])

        # Deleting model 'InvMetaType'
        db.delete_table('eve_db_invmetatype')

        # Deleting model 'InvFlag'
        db.delete_table('eve_db_invflag')

        # Deleting model 'DgmAttributeCategory'
        db.delete_table('eve_db_dgmattributecategory')

        # Deleting model 'DgmAttributeType'
        db.delete_table('eve_db_dgmattributetype')

        # Deleting model 'DgmTypeAttribute'
        db.delete_table('eve_db_dgmtypeattribute')

        # Removing unique constraint on 'DgmTypeAttribute', fields ['inventory_type', 'attribute']
        db.delete_unique('eve_db_dgmtypeattribute', ['inventory_type_id', 'attribute_id'])

        # Deleting model 'InvBlueprintType'
        db.delete_table('eve_db_invblueprinttype')

        # Deleting model 'DgmEffect'
        db.delete_table('eve_db_dgmeffect')

        # Deleting model 'DgmTypeEffect'
        db.delete_table('eve_db_dgmtypeeffect')

        # Removing unique constraint on 'DgmTypeEffect', fields ['type', 'effect']
        db.delete_unique('eve_db_dgmtypeeffect', ['type_id', 'effect_id'])

        # Deleting model 'InvPOSResourcePurpose'
        db.delete_table('eve_db_invposresourcepurpose')

        # Deleting model 'InvPOSResource'
        db.delete_table('eve_db_invposresource')

        # Removing unique constraint on 'InvPOSResource', fields ['control_tower_type', 'resource_type']
        db.delete_unique('eve_db_invposresource', ['control_tower_type_id', 'resource_type_id'])

        # Deleting model 'InvTypeReaction'
        db.delete_table('eve_db_invtypereaction')

        # Removing unique constraint on 'InvTypeReaction', fields ['reaction_type', 'input', 'type']
        db.delete_unique('eve_db_invtypereaction', ['reaction_type_id', 'input', 'type_id'])

        # Deleting model 'InvContrabandType'
        db.delete_table('eve_db_invcontrabandtype')

        # Removing unique constraint on 'InvContrabandType', fields ['faction', 'type']
        db.delete_unique('eve_db_invcontrabandtype', ['faction_id', 'type_id'])

        # Deleting model 'MapUniverse'
        db.delete_table('eve_db_mapuniverse')

        # Deleting model 'MapRegion'
        db.delete_table('eve_db_mapregion')

        # Deleting model 'MapRegionJump'
        db.delete_table('eve_db_mapregionjump')

        # Removing unique constraint on 'MapRegionJump', fields ['from_region', 'to_region']
        db.delete_unique('eve_db_mapregionjump', ['from_region_id', 'to_region_id'])

        # Deleting model 'MapConstellation'
        db.delete_table('eve_db_mapconstellation')

        # Deleting model 'MapConstellationJump'
        db.delete_table('eve_db_mapconstellationjump')

        # Removing unique constraint on 'MapConstellationJump', fields ['from_constellation', 'to_constellation']
        db.delete_unique('eve_db_mapconstellationjump', ['from_constellation_id', 'to_constellation_id'])

        # Deleting model 'MapSolarSystem'
        db.delete_table('eve_db_mapsolarsystem')

        # Deleting model 'MapSolarSystemJump'
        db.delete_table('eve_db_mapsolarsystemjump')

        # Removing unique constraint on 'MapSolarSystemJump', fields ['from_solar_system', 'to_solar_system']
        db.delete_unique('eve_db_mapsolarsystemjump', ['from_solar_system_id', 'to_solar_system_id'])

        # Deleting model 'MapJump'
        db.delete_table('eve_db_mapjump')

        # Deleting model 'MapCelestialStatistic'
        db.delete_table('eve_db_mapcelestialstatistic')

        # Deleting model 'MapDenormalize'
        db.delete_table('eve_db_mapdenormalize')

        # Deleting model 'MapLandmark'
        db.delete_table('eve_db_maplandmark')

        # Deleting model 'ChrRace'
        db.delete_table('eve_db_chrrace')

        # Deleting model 'ChrBloodline'
        db.delete_table('eve_db_chrbloodline')

        # Deleting model 'ChrAncestry'
        db.delete_table('eve_db_chrancestry')

        # Deleting model 'ChrAttribute'
        db.delete_table('eve_db_chrattribute')

        # Deleting model 'ChrFaction'
        db.delete_table('eve_db_chrfaction')

        # Deleting model 'CrpActivity'
        db.delete_table('eve_db_crpactivity')

        # Deleting model 'CrpNPCCorporation'
        db.delete_table('eve_db_crpnpccorporation')

        # Deleting model 'CrpNPCDivision'
        db.delete_table('eve_db_crpnpcdivision')

        # Deleting model 'CrpNPCCorporationDivision'
        db.delete_table('eve_db_crpnpccorporationdivision')

        # Removing unique constraint on 'CrpNPCCorporationDivision', fields ['corporation', 'division']
        db.delete_unique('eve_db_crpnpccorporationdivision', ['corporation_id', 'division_id'])

        # Deleting model 'CrpNPCCorporationTrade'
        db.delete_table('eve_db_crpnpccorporationtrade')

        # Removing unique constraint on 'CrpNPCCorporationTrade', fields ['corporation', 'type']
        db.delete_unique('eve_db_crpnpccorporationtrade', ['corporation_id', 'type_id'])

        # Deleting model 'CrpNPCCorporationResearchField'
        db.delete_table('eve_db_crpnpccorporationresearchfield')

        # Removing unique constraint on 'CrpNPCCorporationResearchField', fields ['skill', 'corporation']
        db.delete_unique('eve_db_crpnpccorporationresearchfield', ['skill_id', 'corporation_id'])

        # Deleting model 'AgtAgentType'
        db.delete_table('eve_db_agtagenttype')

        # Deleting model 'AgtAgent'
        db.delete_table('eve_db_agtagent')

        # Deleting model 'AgtConfig'
        db.delete_table('eve_db_agtconfig')

        # Removing unique constraint on 'AgtConfig', fields ['agent', 'key']
        db.delete_unique('eve_db_agtconfig', ['agent_id', 'key'])

        # Deleting model 'RamActivity'
        db.delete_table('eve_db_ramactivity')

        # Deleting model 'RamAssemblyLineType'
        db.delete_table('eve_db_ramassemblylinetype')

        # Deleting model 'RamAssemblyLine'
        db.delete_table('eve_db_ramassemblyline')

        # Deleting model 'RamAssemblyLineTypeDetailPerCategory'
        db.delete_table('eve_db_ramassemblylinetypedetailpercategory')

        # Removing unique constraint on 'RamAssemblyLineTypeDetailPerCategory', fields ['assembly_line_type', 'category']
        db.delete_unique('eve_db_ramassemblylinetypedetailpercategory', ['assembly_line_type_id', 'category_id'])

        # Deleting model 'RamAssemblyLineTypeDetailPerGroup'
        db.delete_table('eve_db_ramassemblylinetypedetailpergroup')

        # Removing unique constraint on 'RamAssemblyLineTypeDetailPerGroup', fields ['assembly_line_type', 'group']
        db.delete_unique('eve_db_ramassemblylinetypedetailpergroup', ['assembly_line_type_id', 'group_id'])

        # Deleting model 'RamAssemblyLineStations'
        db.delete_table('eve_db_ramassemblylinestations')

        # Removing unique constraint on 'RamAssemblyLineStations', fields ['station', 'assembly_line_type']
        db.delete_unique('eve_db_ramassemblylinestations', ['station_id', 'assembly_line_type_id'])

        # Deleting model 'RamTypeRequirement'
        db.delete_table('eve_db_ramtyperequirement')

        # Removing unique constraint on 'RamTypeRequirement', fields ['type', 'activity_type', 'required_type']
        db.delete_unique('eve_db_ramtyperequirement', ['type_id', 'activity_type_id', 'required_type_id'])

        # Deleting model 'StaService'
        db.delete_table('eve_db_staservice')

        # Deleting model 'StaStationType'
        db.delete_table('eve_db_stastationtype')

        # Deleting model 'StaOperation'
        db.delete_table('eve_db_staoperation')

        # Deleting model 'StaStation'
        db.delete_table('eve_db_stastation')

        # Deleting model 'StaOperationServices'
        db.delete_table('eve_db_staoperationservices')

        # Removing unique constraint on 'StaOperationServices', fields ['operation', 'service']
        db.delete_unique('eve_db_staoperationservices', ['operation_id', 'service_id'])

        # Deleting model 'CrtCategory'
        db.delete_table('eve_db_crtcategory')

        # Deleting model 'CrtClass'
        db.delete_table('eve_db_crtclass')

        # Deleting model 'CrtCertificate'
        db.delete_table('eve_db_crtcertificate')

        # Deleting model 'CrtRelationship'
        db.delete_table('eve_db_crtrelationship')

        # Deleting model 'CrtRecommendation'
        db.delete_table('eve_db_crtrecommendation')

        # Deleting model 'PlanetSchematic'
        db.delete_table('eve_db_planetschematic')

        # Deleting model 'PlanetSchematicsPinMap'
        db.delete_table('eve_db_planetschematicspinmap')

        # Removing unique constraint on 'PlanetSchematicsPinMap', fields ['schematic', 'type']
        db.delete_unique('eve_db_planetschematicspinmap', ['schematic_id', 'type_id'])

        # Deleting model 'PlanetSchematicsTypeMap'
        db.delete_table('eve_db_planetschematicstypemap')

        # Removing unique constraint on 'PlanetSchematicsTypeMap', fields ['schematic', 'type']
        db.delete_unique('eve_db_planetschematicstypemap', ['schematic_id', 'type_id'])


    models = {
        'eve_api.apiplayeralliance': {
            'Meta': {'object_name': 'ApiPlayerAlliance'},
            'api_last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_founded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'eve_db.agtagent': {
            'Meta': {'object_name': 'AgtAgent'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCDivision']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapDenormalize']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.AgtAgentType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.agtagenttype': {
            'Meta': {'object_name': 'AgtAgentType'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'eve_db.agtconfig': {
            'Meta': {'unique_together': "(('agent', 'key'),)", 'object_name': 'AgtConfig'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.AgtAgent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'eve_db.chrancestry': {
            'Meta': {'object_name': 'ChrAncestry'},
            'bloodline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrBloodline']", 'null': 'True', 'blank': 'True'}),
            'charisma_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'intelligence_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'memory_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'perception_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'willpower_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'eve_db.chrattribute': {
            'Meta': {'object_name': 'ChrAttribute'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'eve_db.chrbloodline': {
            'Meta': {'object_name': 'ChrBloodline'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'female_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'male_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bloodline_set'", 'null': 'True', 'to': "orm['eve_db.ChrRace']"}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_female_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_male_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'starter_ship_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bloodline_starter_ship_set'", 'null': 'True', 'to': "orm['eve_db.InvType']"}),
            'starting_charisma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'starting_intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'starting_memory': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'starting_perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'starting_willpower': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'eve_db.chrfaction': {
            'Meta': {'object_name': 'ChrFaction'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'faction_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'size_factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'faction_set'", 'null': 'True', 'to': "orm['eve_db.MapSolarSystem']"}),
            'station_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'station_system_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'eve_db.chrrace': {
            'Meta': {'object_name': 'ChrRace'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'eve_db.crpactivity': {
            'Meta': {'object_name': 'CrpActivity'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eve_db.crpnpccorporation': {
            'Meta': {'object_name': 'CrpNPCCorporation'},
            'border_systems': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'corridor_systems': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enemy_corp': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'enemy_of_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'extent': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']", 'null': 'True', 'blank': 'True'}),
            'friendly_corp': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'friendly_with_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'fringe_systems': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hub_systems': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'initial_share_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'investor1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invested1_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'investor1_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'investor2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invested2_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'investor2_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'investor3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invested3_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'investor3_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'investor4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invested4_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'investor4_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'public_share_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'size_factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'station_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'station_system_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stations_are_scattered': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'eve_db.crpnpccorporationdivision': {
            'Meta': {'unique_together': "(('corporation', 'division'),)", 'object_name': 'CrpNPCCorporationDivision'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']"}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCDivision']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.crpnpccorporationresearchfield': {
            'Meta': {'unique_together': "(('skill', 'corporation'),)", 'object_name': 'CrpNPCCorporationResearchField'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.crpnpccorporationtrade': {
            'Meta': {'unique_together': "(('corporation', 'type'),)", 'object_name': 'CrpNPCCorporationTrade'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.crpnpcdivision': {
            'Meta': {'object_name': 'CrpNPCDivision'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'leader_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'eve_db.crtcategory': {
            'Meta': {'object_name': 'CrtCategory'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'eve_db.crtcertificate': {
            'Meta': {'object_name': 'CrtCertificate'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrtCategory']", 'null': 'True', 'blank': 'True'}),
            'cert_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrtClass']", 'null': 'True', 'blank': 'True'}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'icon_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'})
        },
        'eve_db.crtclass': {
            'Meta': {'object_name': 'CrtClass'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'eve_db.crtrecommendation': {
            'Meta': {'object_name': 'CrtRecommendation'},
            'certificate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrtCertificate']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'recommendation_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.crtrelationship': {
            'Meta': {'object_name': 'CrtRelationship'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_crtrelationship_set'", 'null': 'True', 'to': "orm['eve_db.CrtCertificate']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_crtrelationship_set'", 'null': 'True', 'to': "orm['eve_db.CrtCertificate']"}),
            'parent_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.dgmattributecategory': {
            'Meta': {'object_name': 'DgmAttributeCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'eve_db.dgmattributetype': {
            'Meta': {'object_name': 'DgmAttributeType'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.DgmAttributeCategory']", 'null': 'True', 'blank': 'True'}),
            'defaultvalue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'high_is_good': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_stackable': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEUnit']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.dgmeffect': {
            'Meta': {'object_name': 'DgmEffect'},
            'category': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'disallow_auto_repeat': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'discharge_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectdischargeattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'distribution': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'duration_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectdurationeattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'falloff_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectfalloffattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'fitting_usage_chance_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectfittingusagechanceattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'has_electronic_chance': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'has_propulsion_chance': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'has_range_chance': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_assistance': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_offensive': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_warp_safe': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'npc_activation_chance_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectnpcactivationchanceattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'npc_usage_chance_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectnpcusagechanceattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'post_expression': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pre_expression': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'range_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectrangeattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'sfx_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tracking_speed_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffecttrackingspeedattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"})
        },
        'eve_db.dgmtypeattribute': {
            'Meta': {'unique_together': "(('inventory_type', 'attribute'),)", 'object_name': 'DgmTypeAttribute'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.DgmAttributeType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"}),
            'value_float': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'value_int': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.dgmtypeeffect': {
            'Meta': {'unique_together': "(('type', 'effect'),)", 'object_name': 'DgmTypeEffect'},
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.DgmEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"})
        },
        'eve_db.evegraphic': {
            'Meta': {'object_name': 'EVEGraphic'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'icon_filename': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_obsolete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'eve_db.evename': {
            'Meta': {'object_name': 'EveName'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvCategory']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.eveunit': {
            'Meta': {'object_name': 'EVEUnit'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'eve_db.invblueprinttype': {
            'Meta': {'object_name': 'InvBlueprintType'},
            'blueprint_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blueprint_type_set'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['eve_db.InvType']"}),
            'material_modifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_production_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent_blueprint_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_blueprint_type_set'", 'null': 'True', 'to': "orm['eve_db.InvType']"}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blueprint_product_type_set'", 'to': "orm['eve_db.InvType']"}),
            'productivity_modifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'research_copy_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'research_material_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'research_productivity_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'research_tech_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tech_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'waste_factor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.invcategory': {
            'Meta': {'object_name': 'InvCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'eve_db.invcontrabandtype': {
            'Meta': {'unique_together': "(('faction', 'type'),)", 'object_name': 'InvContrabandType'},
            'attack_min_sec': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'confiscate_min_sec': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']"}),
            'fine_by_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'standing_loss': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"})
        },
        'eve_db.invflag': {
            'Meta': {'object_name': 'InvFlag'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'eve_db.invgroup': {
            'Meta': {'object_name': 'InvGroup'},
            'allow_anchoring': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'allow_manufacture': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'allow_recycle': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvCategory']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_anchored': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_fittable_non_singleton': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'use_base_price': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'eve_db.invmarketgroup': {
            'Meta': {'object_name': 'InvMarketGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'has_items': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvMarketGroup']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.invmetagroup': {
            'Meta': {'object_name': 'InvMetaGroup'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'eve_db.invmetatype': {
            'Meta': {'object_name': 'InvMetaType'},
            'meta_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvMetaGroup']"}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventorymetatype_parent_type_set'", 'to': "orm['eve_db.InvType']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventorymetatype_type_set'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.invposresource': {
            'Meta': {'unique_together': "(('control_tower_type', 'resource_type'),)", 'object_name': 'InvPOSResource'},
            'control_tower_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tower_resource_set'", 'to': "orm['eve_db.InvType']"}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_security_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvPOSResourcePurpose']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resource_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pos_resource_set'", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.invposresourcepurpose': {
            'Meta': {'object_name': 'InvPOSResourcePurpose'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'})
        },
        'eve_db.invtype': {
            'Meta': {'object_name': 'InvType'},
            'base_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'chance_of_duplicating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'market_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvMarketGroup']", 'null': 'True', 'blank': 'True'}),
            'mass': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'portion_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrRace']", 'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.invtypematerial': {
            'Meta': {'unique_together': "(('type', 'material_type'),)", 'object_name': 'InvTypeMaterial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemtype_set'", 'to': "orm['eve_db.InvType']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'material_set'", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.invtypereaction': {
            'Meta': {'unique_together': "(('reaction_type', 'input', 'type'),)", 'object_name': 'InvTypeReaction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reaction_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventorytypereactions_reaction_type_set'", 'to': "orm['eve_db.InvType']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventorytypereactions_type_set'", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.mapcelestialstatistic': {
            'Meta': {'object_name': 'MapCelestialStatistic'},
            'age': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'celestial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapDenormalize']", 'unique': 'True', 'primary_key': 'True'}),
            'density': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eccentricity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'escape_velocity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_fragmented': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'life': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'luminousity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mass': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mass_dust': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mass_gas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'orbit_period': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'orbit_radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pressure': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rotation_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'spectral_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'surface_gravity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapconstellation': {
            'Meta': {'object_name': 'MapConstellation'},
            'alliance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_api.ApiPlayerAlliance']", 'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'sovereignty_grace_start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sovereignty_start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapconstellationjump': {
            'Meta': {'unique_together': "(('from_constellation', 'to_constellation'),)", 'object_name': 'MapConstellationJump'},
            'from_constellation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellation_jumps_from_constellation_set'", 'to': "orm['eve_db.MapConstellation']"}),
            'from_region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellation_jumps_from_region_set'", 'to': "orm['eve_db.MapRegion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_constellation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellation_jumps_to_constellation_set'", 'to': "orm['eve_db.MapConstellation']"}),
            'to_region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellation_jumps_to_region_set'", 'to': "orm['eve_db.MapRegion']"})
        },
        'eve_db.mapdenormalize': {
            'Meta': {'object_name': 'MapDenormalize'},
            'celestial_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapConstellation']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'orbit_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'orbit_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapjump': {
            'Meta': {'object_name': 'MapJump'},
            'destination_gate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stargate_jump_destination_set'", 'to': "orm['eve_db.MapDenormalize']"}),
            'origin_gate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stargate_jump_origin_set'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['eve_db.MapDenormalize']"})
        },
        'eve_db.maplandmark': {
            'Meta': {'object_name': 'MapLandmark'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EVEGraphic']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'url_2d': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapregion': {
            'Meta': {'object_name': 'MapRegion'},
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapregionjump': {
            'Meta': {'unique_together': "(('from_region', 'to_region'),)", 'object_name': 'MapRegionJump'},
            'from_region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'region_jumps_from_region_set'", 'to': "orm['eve_db.MapRegion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'region_jumps_to_region_set'", 'to': "orm['eve_db.MapRegion']"})
        },
        'eve_db.mapsolarsystem': {
            'Meta': {'object_name': 'MapSolarSystem'},
            'alliance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_api.ApiPlayerAlliance']", 'null': 'True', 'blank': 'True'}),
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapConstellation']", 'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solarsystem_set'", 'null': 'True', 'to': "orm['eve_db.ChrFaction']"}),
            'has_interconstellational_link': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'has_interregional_link': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_border_system': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_corridor_system': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_fringe_system': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_hub_system': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_international': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'luminosity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'security_class': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'security_level': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sovereignty_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sovereignty_start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sun_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapsolarsystemjump': {
            'Meta': {'unique_together': "(('from_solar_system', 'to_solar_system'),)", 'object_name': 'MapSolarSystemJump'},
            'from_constellation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solar_system_jumps_from_constellation_set'", 'null': 'True', 'to': "orm['eve_db.MapConstellation']"}),
            'from_region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solar_system_jumps_from_region_set'", 'null': 'True', 'to': "orm['eve_db.MapRegion']"}),
            'from_solar_system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solar_system_jumps_from_solar_system_set'", 'to': "orm['eve_db.MapSolarSystem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_constellation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solar_system_jumps_to_constellation_set'", 'null': 'True', 'to': "orm['eve_db.MapConstellation']"}),
            'to_region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solar_system_jumps_to_region_set'", 'null': 'True', 'to': "orm['eve_db.MapRegion']"}),
            'to_solar_system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solar_system_jumps_to_solar_system_set'", 'to': "orm['eve_db.MapSolarSystem']"})
        },
        'eve_db.mapuniverse': {
            'Meta': {'object_name': 'MapUniverse'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.planetschematic': {
            'Meta': {'object_name': 'PlanetSchematic'},
            'cycle_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pin_map': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'usable_schematics'", 'symmetrical': 'False', 'through': "orm['eve_db.PlanetSchematicsPinMap']", 'to': "orm['eve_db.InvType']"}),
            'type_map': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'used_with_schematic'", 'symmetrical': 'False', 'through': "orm['eve_db.PlanetSchematicsTypeMap']", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.planetschematicspinmap': {
            'Meta': {'unique_together': "(('schematic', 'type'),)", 'object_name': 'PlanetSchematicsPinMap'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schematic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.PlanetSchematic']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"})
        },
        'eve_db.planetschematicstypemap': {
            'Meta': {'unique_together': "(('schematic', 'type'),)", 'object_name': 'PlanetSchematicsTypeMap'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_input': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'schematic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.PlanetSchematic']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"})
        },
        'eve_db.ramactivity': {
            'Meta': {'object_name': 'RamActivity'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'icon_filename': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'})
        },
        'eve_db.ramassemblyline': {
            'Meta': {'object_name': 'RamAssemblyLine'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamActivity']", 'null': 'True', 'blank': 'True'}),
            'assembly_line_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamAssemblyLineType']", 'null': 'True', 'blank': 'True'}),
            'cost_install': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cost_per_hour': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'discount_per_good_standing_point': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'maximum_char_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'maximum_corp_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_char_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_corp_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_standing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaStation']", 'null': 'True', 'blank': 'True'}),
            'surcharge_per_bad_standing_point': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ui_grouping_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramassemblylinestations': {
            'Meta': {'unique_together': "(('station', 'assembly_line_type'),)", 'object_name': 'RamAssemblyLineStations'},
            'assembly_line_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamAssemblyLineType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaStation']"}),
            'station_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaStationType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramassemblylinetype': {
            'Meta': {'object_name': 'RamAssemblyLineType'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamActivity']", 'null': 'True', 'blank': 'True'}),
            'base_material_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'base_time_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'min_cost_per_hour': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramassemblylinetypedetailpercategory': {
            'Meta': {'unique_together': "(('assembly_line_type', 'category'),)", 'object_name': 'RamAssemblyLineTypeDetailPerCategory'},
            'assembly_line_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamAssemblyLineType']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'time_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramassemblylinetypedetailpergroup': {
            'Meta': {'unique_together': "(('assembly_line_type', 'group'),)", 'object_name': 'RamAssemblyLineTypeDetailPerGroup'},
            'assembly_line_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamAssemblyLineType']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'time_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramtyperequirement': {
            'Meta': {'unique_together': "(('type', 'activity_type', 'required_type'),)", 'object_name': 'RamTypeRequirement'},
            'activity_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamActivity']"}),
            'damage_per_job': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recycle': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'required_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_type'", 'to': "orm['eve_db.InvType']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'type_requirement'", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.staoperation': {
            'Meta': {'object_name': 'StaOperation'},
            'activity_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'amarr_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'amarr_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'border': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'caldari_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'caldari_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'corridor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fringe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gallente_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gallente_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'hub': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'jove_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jove_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'minmatar_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'minmatar_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.staoperationservices': {
            'Meta': {'unique_together': "(('operation', 'service'),)", 'object_name': 'StaOperationServices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaOperation']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaService']"})
        },
        'eve_db.staservice': {
            'Meta': {'object_name': 'StaService'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eve_db.stastation': {
            'Meta': {'object_name': 'StaStation'},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapConstellation']", 'null': 'True', 'blank': 'True'}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'docking_cost_per_volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'max_ship_volume_dockable': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'office_rental_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaOperation']", 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'reprocessing_efficiency': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reprocessing_hangar_flag': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reprocessing_stations_take': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'security': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaStationType']", 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.stastationtype': {
            'Meta': {'object_name': 'StaStationType'},
            'dock_entry_x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_entry_y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_entry_z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_orientation_x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_orientation_y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_orientation_z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'docking_bay_graphic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'docking_bay_graphic'", 'null': 'True', 'to': "orm['eve_db.EVEGraphic']"}),
            'hangar_graphic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hangar_graphic'", 'null': 'True', 'to': "orm['eve_db.EVEGraphic']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_conquerable': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'office_slots': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaOperation']", 'null': 'True', 'blank': 'True'}),
            'reprocessing_efficiency': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['eve_db']
