"""
Import NPC corp/agent data.
"""
from eve_db.models import npc as npc_models
from eve_db.models.inventory import InvName
from importer_classes import SQLImporter
from eve_db.models.npc import AgtAgent


class Importer_crpActivities(SQLImporter):
    model = npc_models.CrpActivity
    pks = (('id', 'activityID'),)
    field_map = (('name', 'activityName'),
                 ('description', 'description'))


class Importer_crpNPCCorporationDivisions(SQLImporter):
    DEPENDENCIES = ['crpNPCDivisions', 'crpNPCCorporations']
    model = npc_models.CrpNPCCorporationDivision
    pks = (('corporation', 'corporationID'), ('division', 'divisionID'))
    field_map = (('size', 'size'),)


class Importer_crpNPCCorporationTrades(SQLImporter):
    DEPENDENCIES = ['invTypes', 'crpNPCCorporations']
    model = npc_models.CrpNPCCorporationTrade
    pks = (('corporation', 'corporationID'), ('type', 'typeID'))


class Importer_crpNPCCorporationResearchFields(SQLImporter):
    DEPENDENCIES = ['invTypes', 'crpNPCCorporations']
    model = npc_models.CrpNPCCorporationResearchField
    pks = (('corporation', 'corporationID'), ('skill', 'skillID'))


class Importer_agtAgentTypes(SQLImporter):
    model = npc_models.AgtAgentType
    pks = (('id', 'agentTypeID'),)
    field_map = (('name', 'agentType'),)


# Need to keep this mostly the old way due to all the self-referencing
# foreign keys.
class Importer_crpNPCCorporations(SQLImporter):
    DEPENDENCIES = ['chrFactions', 'invNames', 'mapSolarSystems']
    model = npc_models.CrpNPCCorporation

    def import_row(self, row):
        imp_obj, created = self.model.objects.get_or_create(id=row['corporationID'])
        imp_obj.name = InvName.objects.get(id=row['corporationID']).name
        imp_obj.size = row['size']
        imp_obj.extent = row['extent']

        if row['solarSystemID']:
            imp_obj.solar_system_id = row['solarSystemID']

        if row['investorID1']:
            investor1, created = self.model.objects.get_or_create(id=row['investorID1'])
            imp_obj.investor1 = investor1
            imp_obj.investor1_shares = row['investorShares1']

        if row['investorID2']:
            investor2, created = self.model.objects.get_or_create(id=row['investorID2'])
            imp_obj.investor2 = investor2
            imp_obj.investor2_shares = row['investorShares2']

        if row['investorID3']:
            investor3, created = self.model.objects.get_or_create(id=row['investorID3'])
            imp_obj.investor3 = investor3
            imp_obj.investor3_shares = row['investorShares3']

        if row['investorID4']:
            investor4, created = self.model.objects.get_or_create(id=row['investorID4'])
            imp_obj.investor4 = investor4
            imp_obj.investor4_shares = row['investorShares4']

        if row['friendID']:
            friend, created = self.model.objects.get_or_create(id=row['friendID'])
            imp_obj.friendly_corp = friend

        if row['enemyID']:
            enemy, created = self.model.objects.get_or_create(id=row['enemyID'])
            imp_obj.enemy_corp = enemy

        if row['iconID']:
            imp_obj.icon_id = row['iconID']

        if row['scattered'] == 1:
            imp_obj.stations_are_scattered = True

        imp_obj.public_share_percent = row['publicShares']
        imp_obj.initial_share_price = row['initialPrice']
        imp_obj.min_security = row['minSecurity']
        imp_obj.fringe_systems = row['fringe']
        imp_obj.corridor_systems = row['corridor']
        imp_obj.hub_systems = row['hub']
        imp_obj.border_systems = row['border']
        imp_obj.faction_id = row['factionID']
        imp_obj.size_factor = row['sizeFactor']
        imp_obj.station_count = row['stationCount']
        imp_obj.station_system_count = row['stationSystemCount']
        imp_obj.description = row['description']
        imp_obj.save()
        # Tell the bulk inserter/updater to skip this
        # We've already saved it.
        return None, None

class Importer_crpNPCDivisions(SQLImporter):
    model = npc_models.CrpNPCDivision
    pks = (('id', 'divisionID'),)
    field_map = (('name', 'divisionName'),
                 ('description', 'description'),
                 ('leader_type', 'leaderType'))


def get_evename_for_agent(agent_id):
    return InvName.objects.get(id=agent_id).name

class Importer_agtAgents(SQLImporter):
    DEPENDENCIES = ['crpNPCDivisions', 'mapDenormalize', 'crpNPCCorporations',
                    'invNames', 'agtAgentTypes']
    model = AgtAgent
    pks = (('id', 'agentID'),)
    field_map = (('division_id', 'divisionID'),
                 ('corporation_id', 'corporationID'),
                 ('location_id', 'locationID'),
                 ('level', 'level'),
                 ('quality', 'quality'),
                 ('type_id', 'agentTypeID'),
                 ('name', 'agentID', get_evename_for_agent))


