"""
Import character data.
"""
from django.db import transaction
from importer_classes import SQLImporter

from eve_db.ccp_importer.importers.importer_classes import parse_char_notnull
from eve_db.models import chr as chr_models
from eve_db.models.map import MapSolarSystem
from eve_db.models.npc import CrpNPCCorporation



class Importer_chrRaces(SQLImporter):
    model = chr_models.ChrRace
    pks = (('id', 'raceID'),)
    field_map = (('name', 'raceName'),
                 ('icon_id', 'iconID'),
                 ('description', 'description', parse_char_notnull),
                 ('short_description', 'shortDescription'))


class Importer_chrAttributes(SQLImporter):
    model = chr_models.ChrAttribute
    pks = (('id', 'attributeID'),)
    field_map = (('name', 'attributeName'),
                 ('icon_id', 'iconID'),
                 ('description', 'description'),
                 ('short_description', 'shortDescription'),
                 ('notes', 'notes'))


class Importer_chrFactions(SQLImporter):
    DEPENDENCIES = ['chrRaces', 'mapSolarSystems', 'crpNPCCorporations']
    model = chr_models.ChrFaction

    def import_row(self, row):
        # We need these queries because of circular dependencies
        # chrFactions has few records so it has minimal impact
        solar_system = None
        if row['solarSystemID']:
            solar_system = MapSolarSystem.objects.get_or_create(id=row['solarSystemID'])[0]

        corporation = None
        if row['corporationID']:
            corporation = CrpNPCCorporation.objects.get_or_create(id=row['corporationID'])[0]
        # Make sure to commit this or we'll get a transaction management error
        if solar_system or corporation:
            transaction.commit()

        new_instance = self.model(id=row['factionID'],
                                  name=row['factionName'],
                                  description=row['description'],
                                  solar_system=solar_system,
                                  corporation=corporation,
                                  icon_id=row['iconID'] if row['iconID'] else None,
                                  size_factor=row['sizeFactor'],
                                  station_count=row['stationCount'],
                                  station_system_count=row['stationSystemCount'],
                                  races=row['raceIDs'])
        if self.insert_only:
            return new_instance, True

        try:
            old_instance = self.model.objects.get(id=row['factionID'])
            old_instance.name = row['factionName']
            old_instance.description = row['description']
            old_instance.solar_system = solar_system
            old_instance.corporation = corporation
            old_instance.icon_id = row['iconID'] if row['iconID'] else None
            old_instance.size_factor = row['sizeFactor']
            old_instance.station_count = row['stationCount']
            old_instance.station_system_count = row['stationSystemCount']
            old_instance.races=row['raceIDs']
            return old_instance, False
        except self.model.DoesNotExist:
            return new_instance, True

class Importer_chrBloodlines(SQLImporter):
    DEPENDENCIES = ['chrRaces', 'invTypes', 'crpNPCCorporations']
    model = chr_models.ChrBloodline
    pks = (('id', 'bloodlineID'),)
    field_map = (('name', 'bloodlineName'),
                 ('race_id', 'raceID'),
                 ('description', 'description'),
                 ('male_description', 'maleDescription'),
                 ('female_description', 'femaleDescription'),
                 ('starter_ship_type_id', 'shipTypeID'),
                 ('starting_perception', 'perception'),
                 ('starting_willpower', 'willpower'),
                 ('starting_charisma', 'charisma'),
                 ('starting_memory', 'memory'),
                 ('starting_intelligence', 'intelligence'),
                 ('short_description', 'shortDescription'),
                 ('short_male_description', 'shortMaleDescription'),
                 ('short_female_description', 'shortFemaleDescription'),
                 ('icon_id', 'iconID'))


class Importer_chrAncestries(SQLImporter):
    DEPENDENCIES = ['chrBloodlines', 'invTypes']
    model = chr_models.ChrAncestry
    pks = (('id', 'ancestryID'),)
    field_map = (('name', 'ancestryName'),
                 ('bloodline_id', 'bloodlineID'),
                 ('description', 'description'),
                 ('perception_bonus', 'perception'),
                 ('willpower_bonus', 'willpower'),
                 ('charisma_bonus', 'charisma'),
                 ('memory_bonus', 'memory'),
                 ('intelligence_bonus', 'intelligence'),
                 ('short_description', 'shortDescription'),
                 ('icon_id', 'iconID'))