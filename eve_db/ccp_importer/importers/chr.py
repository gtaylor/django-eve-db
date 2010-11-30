"""
Import character data.
"""
from eve_db.models import *
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

    def import_row(self, row):
        imp_obj, created = ChrFaction.objects.get_or_create(id=row['factionID'])
        imp_obj.name = row['factionName']
        imp_obj.description = row['description']

        if row['solarSystemID']:
            solar_system, ss_created = MapSolarSystem.objects.get_or_create(id=row['solarSystemID'])
            imp_obj.solar_system = solar_system

        if row['corporationID']:
            corp, corp_created = CrpNPCCorporation.objects.get_or_create(id=row['corporationID'])
            imp_obj.corporation = corp

        if row['iconID']:
            imp_obj.icon = EveIcon.objects.get(id=row['iconID'])

        imp_obj.size_factor = row['sizeFactor']
        imp_obj.station_count = row['stationCount']
        imp_obj.station_system_count = row['stationSystemCount']
        imp_obj.save()

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
