"""
Import NPC corp/agent data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_crpActivities(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from crpActivities'):
            imp_obj, created = CorporateActivity.objects.get_or_create(id=row['activityID'])
            imp_obj.name = row['activityName']
            imp_obj.description = row['description']
            imp_obj.save()
        c.close()
    
class Importer_crpNPCCorporations(SQLImporter):
    DEPENDENCIES = ['chrFactions', 'eveNames', 'mapSolarSystems']
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from crpNPCCorporations'):
            imp_obj, created = NPCCorporation.objects.get_or_create(id=row['corporationID'])
            imp_obj.name = EVEInventoryName.objects.get(id=row['corporationID']).name
            imp_obj.size = row['size']
            imp_obj.extent = row['extent']
            
            if row['solarSystemID']:
                ssystem, created = SolarSystem.objects.get_or_create(id=row['solarSystemID'])
                imp_obj.solar_system = ssystem
            
            if row['investorID1']:
                investor1, created = NPCCorporation.objects.get_or_create(id=row['investorID1'])
                imp_obj.investor1 = investor1
                imp_obj.investor1_shares = row['investorShares1']
                
            if row['investorID2']:
                investor2, created = NPCCorporation.objects.get_or_create(id=row['investorID2'])
                imp_obj.investor2 = investor2
                imp_obj.investor2_shares = row['investorShares2']
                
            if row['investorID3']:
                investor3, created = NPCCorporation.objects.get_or_create(id=row['investorID3'])
                imp_obj.investor3 = investor3
                imp_obj.investor3_shares = row['investorShares3']
                
            if row['investorID4']:
                investor4, created = NPCCorporation.objects.get_or_create(id=row['investorID4'])
                imp_obj.investor4 = investor4
                imp_obj.investor4_shares = row['investorShares4']
                
            if row['friendID']:
                friend, created = NPCCorporation.objects.get_or_create(id=row['friendID'])
                imp_obj.friendly_corp = friend
                
            if row['enemyID']:
                enemy, created = NPCCorporation.objects.get_or_create(id=row['enemyID'])
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
            faction, faction_created = EVEFaction.objects.get_or_create(id=row['factionID'])
            imp_obj.faction = faction
            imp_obj.size_factor = row['sizeFactor']
            imp_obj.station_count = row['stationCount']
            imp_obj.station_system_count = row['stationSystemCount']
            imp_obj.description = row['description']
            imp_obj.save()
        c.close()
    
class Importer_crpNPCDivisions(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from crpNPCDivisions'):
            imp_obj, created = NPCCorporationDivision.objects.get_or_create(id=row['divisionID'])
            imp_obj.name = row['divisionName']
            imp_obj.description = row['description']
            imp_obj.leader_type = row['leaderType']
            imp_obj.save()
        c.close()