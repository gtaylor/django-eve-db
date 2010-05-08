"""
Import NPC corp/agent data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_crpActivities(SQLImporter):
    def import_row(self, row):
        imp_obj, created = CrpActivity.objects.get_or_create(id=row['activityID'])
        imp_obj.name = row['activityName']
        imp_obj.description = row['description']
        imp_obj.save()
        
class Importer_crpNPCCorporationDivisions(SQLImporter):
    DEPENDENCIES = ['crpNPCDivisions', 'crpNPCCorporations']
    
    def import_row(self, row):
        corporation = CrpNPCCorporation.objects.get(id=row['corporationID'])
        division = CrpNPCDivision.objects.get(id=row['divisionID'])
        imp_obj, created = CrpNPCCorporationDivision.objects.get_or_create(corporation=corporation,
                                                                           division=division)
        imp_obj.size = row['size']
        imp_obj.save()
        
class Importer_crpNPCCorporationTrades(SQLImporter):
    DEPENDENCIES = ['invTypes', 'crpNPCCorporations']
    
    def import_row(self, row):
        corporation = CrpNPCCorporation.objects.get(id=row['corporationID'])
        type = InvType.objects.get(id=row['typeID'])
        imp_obj, created = CrpNPCCorporationTrade.objects.get_or_create(corporation=corporation,
                                                                        type=type)
        imp_obj.save()
        
class Importer_crpNPCCorporationResearchFields(SQLImporter):
    DEPENDENCIES = ['invTypes', 'crpNPCCorporations']
    
    def import_row(self, row):
        corporation = CrpNPCCorporation.objects.get(id=row['corporationID'])
        skill = InvType.objects.get(id=row['skillID'])
        imp_obj, created = CrpNPCCorporationResearchField.objects.get_or_create(corporation=corporation)
        imp_obj.skill = skill
        imp_obj.save()
        
class Importer_agtAgentTypes(SQLImporter):
    def import_row(self, row):
        imp_obj, created = AgtAgentType.objects.get_or_create(id=row['agentTypeID'])
        imp_obj.name = name=row['agentType']
        imp_obj.save()
    
class Importer_crpNPCCorporations(SQLImporter):
    DEPENDENCIES = ['chrFactions', 'eveNames', 'mapSolarSystems']

    def import_row(self, row):
        imp_obj, created = CrpNPCCorporation.objects.get_or_create(id=row['corporationID'])
        imp_obj.name = EveName.objects.get(id=row['corporationID']).name
        imp_obj.size = row['size']
        imp_obj.extent = row['extent']
        
        if row['solarSystemID']:
            ssystem, created = MapSolarSystem.objects.get_or_create(id=row['solarSystemID'])
            imp_obj.solar_system = ssystem
        
        if row['investorID1']:
            investor1, created = CrpNPCCorporation.objects.get_or_create(id=row['investorID1'])
            imp_obj.investor1 = investor1
            imp_obj.investor1_shares = row['investorShares1']
            
        if row['investorID2']:
            investor2, created = CrpNPCCorporation.objects.get_or_create(id=row['investorID2'])
            imp_obj.investor2 = investor2
            imp_obj.investor2_shares = row['investorShares2']
            
        if row['investorID3']:
            investor3, created = CrpNPCCorporation.objects.get_or_create(id=row['investorID3'])
            imp_obj.investor3 = investor3
            imp_obj.investor3_shares = row['investorShares3']
            
        if row['investorID4']:
            investor4, created = CrpNPCCorporation.objects.get_or_create(id=row['investorID4'])
            imp_obj.investor4 = investor4
            imp_obj.investor4_shares = row['investorShares4']
            
        if row['friendID']:
            friend, created = CrpNPCCorporation.objects.get_or_create(id=row['friendID'])
            imp_obj.friendly_corp = friend
            
        if row['enemyID']:
            enemy, created = CrpNPCCorporation.objects.get_or_create(id=row['enemyID'])
            imp_obj.enemy_corp = enemy
        
        imp_obj.public_share_percent = row['publicShares']
        imp_obj.initial_share_price = row['initialPrice']
        imp_obj.min_security = row['minSecurity']
        
        if row['scattered'] == 1:
            imp_obj.stations_are_scattered = True
            
        imp_obj.fringe_systems = row['fringe']
        imp_obj.corridor_systems = row['corridor']
        imp_obj.hub_systems = row['hub']
        imp_obj.border_systems = row['border']
        faction, faction_created = ChrFaction.objects.get_or_create(id=row['factionID'])
        imp_obj.faction = faction
        imp_obj.size_factor = row['sizeFactor']
        imp_obj.station_count = row['stationCount']
        imp_obj.station_system_count = row['stationSystemCount']
        imp_obj.description = row['description']
        imp_obj.save()
    
class Importer_crpNPCDivisions(SQLImporter):
    def import_row(self, row):
        imp_obj, created = CrpNPCDivision.objects.get_or_create(id=row['divisionID'])
        imp_obj.name = row['divisionName']
        imp_obj.description = row['description']
        imp_obj.leader_type = row['leaderType']
        imp_obj.save()
        
class Importer_agtAgents(SQLImporter):
    DEPENDENCIES = ['crpNPCDivisions', 'mapDenormalize', 'crpNPCCorporations',
                    'eveNames', 'agtAgentTypes']
    def import_row(self, row):
        imp_obj, created = AgtAgent.objects.get_or_create(id=row['agentID'])
        imp_obj.division = CrpNPCDivision.objects.get(id=row['divisionID'])
        imp_obj.corporation = CrpNPCCorporation.objects.get(id=row['corporationID'])
        imp_obj.location = MapDenormalize.objects.get(id=row['locationID'])
        imp_obj.level = row['level']
        imp_obj.quality = row['quality']
        imp_obj.type = AgtAgentType.objects.get(id=row['agentTypeID'])
        imp_obj.name = EveName.objects.get(id=row['agentID']).name
        imp_obj.save()
        
class Importer_agtConfig(SQLImporter):
    DEPENDENCIES = ['agtAgents']
    def import_row(self, row):
        agent = AgtAgent.objects.get(id=row['agentID'])
        imp_obj, created = AgtConfig.objects.get_or_create(agent=agent,
                                                                key=row['k'])
        imp_obj.value = row['v']
        imp_obj.save()
