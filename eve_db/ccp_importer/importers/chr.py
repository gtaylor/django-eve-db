"""
Import character data.
"""
from eve_db.models import *
from django.db import transaction
from importer_classes import SQLImporter

class Importer_chrRaces(SQLImporter):
    DEPENDENCIES = ['eveIcons']

    def import_row(self, row):
        imp_obj, created = ChrRace.objects.get_or_create(id=row['raceID'])
        imp_obj.name = row['raceName']
        imp_obj.short_description = row['shortDescription']
        imp_obj.description = row['description']

        icon_id = row['iconID']
        if icon_id:
            imp_obj.icon = EveIcon.objects.get(id=icon_id)

        imp_obj.save()

class Importer_chrAttributes(SQLImporter):
    DEPENDENCIES = ['eveIcons']

    def import_row(self, row):
        imp_obj, created = ChrAttribute.objects.get_or_create(id=row['attributeID'])
        imp_obj.name = row['attributeName']
        imp_obj.short_description = row['shortDescription']
        imp_obj.description = row['description']
        imp_obj.notes = row['notes']

        icon_id = row['iconID']
        if icon_id:
            imp_obj.icon = EveIcon.objects.get(id=icon_id)

        imp_obj.save()

class Importer_chrFactions(SQLImporter):
    DEPENDENCIES = ['eveIcons', 'mapSolarSystems', 'crpNPCCorporations']
    model = ChrFaction

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
                                  station_system_count=row['stationSystemCount'])
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
            return old_instance, False
        except self.model.DoesNotExist:
            return new_instance, True

class Importer_chrBloodlines(SQLImporter):
    DEPENDENCIES = ['chrRaces', 'invTypes', 'crpNPCCorporations', 'eveIcons']

    def import_row(self, row):
        imp_obj, created = ChrBloodline.objects.get_or_create(id=row['bloodlineID'])
        imp_obj.name = row['bloodlineName']
        imp_obj.race = ChrRace.objects.get(id=row['raceID'])
        imp_obj.description = row['description']
        imp_obj.male_description = row['maleDescription']
        imp_obj.female_description = row['femaleDescription']
        starter_ship, ship_created = InvType.objects.get_or_create(id=row['shipTypeID'])
        imp_obj.starter_ship_type = starter_ship
        imp_obj.starting_perception = row['perception']
        imp_obj.starting_willpower = row['willpower']
        imp_obj.starting_charisma = row['charisma']
        imp_obj.starting_memory = row['memory']
        imp_obj.starting_intelligence = row['intelligence']
        imp_obj.short_description = row['shortDescription']
        imp_obj.short_male_description = row['shortMaleDescription']
        imp_obj.short_female_description = row['shortFemaleDescription']

        icon_id = row['iconID']
        if icon_id:
            imp_obj.icon = EveIcon.objects.get(id=icon_id)

        imp_obj.save()

class Importer_chrAncestries(SQLImporter):
    DEPENDENCIES = ['chrBloodlines', 'invTypes', 'eveIcons']

    def import_row(self, row):
        imp_obj, created = ChrAncestry.objects.get_or_create(id=row['ancestryID'])
        imp_obj.name = row['ancestryName']
        imp_obj.bloodline = ChrBloodline.objects.get(id=row['bloodlineID'])
        imp_obj.description = row['description']
        imp_obj.perception_bonus = row['perception']
        imp_obj.willpower_bonus = row['willpower']
        imp_obj.charisma_bonus = row['charisma']
        imp_obj.memory_bonus = row['memory']
        imp_obj.intelligence_bonus = row['intelligence']
        imp_obj.short_description = row['shortDescription']

        icon_id = row['iconID']
        if icon_id:
            imp_obj.icon = EveIcon.objects.get(id=icon_id)

        imp_obj.save()
