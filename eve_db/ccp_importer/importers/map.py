"""
Import map data.
"""
from eve_db.models import *
from importer_classes import SQLImporter

class Importer_mapUniverse(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from mapUniverse'):
            imp_obj, created = Universe.objects.get_or_create(id=row['universeID'])
            if row['universeName']:
                imp_obj.name = row['universeName']
            imp_obj.x = row['x']
            imp_obj.x_min = row['xMin']
            imp_obj.x_max = row['xMax']
            imp_obj.y = row['y']
            imp_obj.y_min = row['yMin']
            imp_obj.y_max = row['yMax']
            imp_obj.z = row['z']
            imp_obj.z_min = row['zMin']
            imp_obj.z_max = row['zMax']
            imp_obj.radius = row['radius']
            imp_obj.save()
        c.close()
    
class Importer_mapRegions(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from mapRegions'):
            imp_obj, created = Region.objects.get_or_create(id=row['regionID'])
            imp_obj.name = row['regionName']
            imp_obj.x = row['x']
            imp_obj.x_min = row['xMin']
            imp_obj.x_max = row['xMax']
            imp_obj.y = row['y']
            imp_obj.y_min = row['yMin']
            imp_obj.y_max = row['yMax']
            imp_obj.z = row['z']
            imp_obj.z_min = row['zMin']
            imp_obj.z_max = row['zMax']
            if row['factionID']:
                faction, faction_created = Faction.objects.get_or_create(id=row['factionID'])
                imp_obj.faction = faction
            imp_obj.radius = row['radius']
            imp_obj.save()
        c.close()

class Importer_mapConstellations(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from mapConstellations'):
            imp_obj, created = Constellation.objects.get_or_create(id=row['constellationID'])
            imp_obj.name = row['constellationName']
            imp_obj.x = row['x']
            imp_obj.x_min = row['xMin']
            imp_obj.x_max = row['xMax']
            imp_obj.y = row['y']
            imp_obj.y_min = row['yMin']
            imp_obj.y_max = row['yMax']
            imp_obj.z = row['z']
            imp_obj.z_min = row['zMin']
            imp_obj.z_max = row['zMax']
            imp_obj.radius = row['radius']
    
            if row['regionID']:
                region, region_created = Region.objects.get_or_create(id=row['regionID'])
                imp_obj.region = region
                
            if row['factionID']:
                faction, faction_created = Faction.objects.get_or_create(id=row['factionID'])
                imp_obj.faction = faction
    
            imp_obj.save()
        c.close()
    
class Importer_mapSolarSystems(SQLImporter):
    def run_importer(self, conn):
        c = conn.cursor()
        
        for row in c.execute('select * from mapSolarSystems'):
            imp_obj, created = SolarSystem.objects.get_or_create(id=row['solarSystemID'])
            imp_obj.name = row['solarSystemName']
            imp_obj.x = row['x']
            imp_obj.x_min = row['xMin']
            imp_obj.x_max = row['xMax']
            imp_obj.y = row['y']
            imp_obj.y_min = row['yMin']
            imp_obj.y_max = row['yMax']
            imp_obj.z = row['z']
            imp_obj.z_min = row['zMin']
            imp_obj.z_max = row['zMax']
            imp_obj.radius = row['radius']
            imp_obj.luminosity = row['luminosity']
            imp_obj.security_level = row['security']
            if row['securityClass']:
                imp_obj.security_class = row['securityClass']
            
            if row['border'] == 1:
                imp_obj.is_border_system = True
                
            if row['fringe'] == 1:
                imp_obj.is_fringe_system = True
                
            if row['corridor'] == 1:
                imp_obj.is_corridor_system = True
                
            if row['hub'] == 1:
                imp_obj.is_hub_system = True
                
            if row['international'] == 1:
                imp_obj.is_international = True
                
            if row['regional'] == 1:
                imp_obj.has_interregional_link = True
                
            if row['constellation'] == 1:
                imp_obj.has_interconstellational_link = True
    
            if row['regionID']:
                region, region_created = Region.objects.get_or_create(id=row['regionID'])
                imp_obj.region = region
                
            if row['constellationID']:
                constellation, constellation_created = Constellation.objects.get_or_create(id=row['constellationID'])
                imp_obj.constellation = constellation
                
            if row['sunTypeID']:
                imp_obj.sun_type = EVEInventoryType.objects.get(id=row['sunTypeID'])
                
            if row['factionID']:
                faction, faction_created = Faction.objects.get_or_create(id=row['factionID'])
                imp_obj.faction = faction
    
            imp_obj.save()
        c.close()