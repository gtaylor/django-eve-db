import datetime
import sqlite3
from django.conf import settings
# Import this way for brevity in IMPORT_LIST.
from importers import *
# Import this way as well for getattr()
import importers

# These are references to importer functions. They are ran in the order
# they appear in this list. Any lines that are commented out are importers
# that have not been written yet.
IMPORT_LIST = [Importer_eveIcons,
               Importer_chrFactions,
               Importer_mapRegions,
               Importer_mapRegionJumps,
               Importer_mapConstellations,
               Importer_mapConstellationJumps,
               Importer_agtAgentTypes,
               Importer_crpNPCDivisions,
               Importer_crpActivities,
               Importer_eveGraphics,
               Importer_eveUnits,
               Importer_invMetaGroups,
               Importer_invFlags,
               Importer_invMarketGroups,
               Importer_invControlTowerResourcePurposes,
               Importer_mapUniverse,
               Importer_staServices,
               Importer_ramActivities,
               Importer_ramAssemblyLineTypes,
               Importer_invCategories,
               Importer_invGroups,
               Importer_chrRaces,
               Importer_invTypes,
               Importer_invTypeMaterials,
               Importer_invControlTowerResources,
               Importer_chrBloodlines,
               Importer_chrAncestries,
               Importer_mapSolarSystems,
               Importer_mapSolarSystemJumps,
               Importer_mapDenormalize,
               Importer_mapJumps,
               Importer_mapCelestialStatistics,
               Importer_mapLandmarks,
               Importer_eveNames,
               Importer_invContrabandTypes,
               Importer_invTypeReactions,
               Importer_invBlueprintTypes,
               Importer_invMetaTypes,
               Importer_dgmAttributeCategories,
               Importer_dgmAttributeTypes,
               Importer_dgmTypeAttributes,
               Importer_dgmEffects,
               Importer_dgmTypeEffects,
               Importer_chrAttributes,
               Importer_ramAssemblyLineTypeDetailPerCategory,
               Importer_ramAssemblyLineTypeDetailPerGroup,
               Importer_crpNPCCorporations,
               Importer_crpNPCCorporationDivisions,
               Importer_crpNPCCorporationTrades,
               Importer_crpNPCCorporationResearchFields,
               Importer_staStationTypes,
               Importer_staOperations,
               Importer_staStations,
               Importer_ramAssemblyLines,
               Importer_staOperationServices,
               Importer_ramAssemblyLineStations,
               Importer_agtAgents,
               Importer_agtConfig,
               Importer_crtCategories,
               Importer_crtClasses,
               Importer_crtCertificates,
               Importer_crtRelationships,
               Importer_crtRecommendations,
               Importer_ramTypeRequirements,
               Importer_planetSchematics,
               Importer_planetSchematicsPinMap,
               Importer_planetSchematicsTypeMap
               ]

def order_importers(importer_classes):
    """
    Given a list of importer classes, order them based on their dependencies.
    
    importer_classes: (list) References to the importer classes to run.
    """
    ordered = []
    for importer_class in IMPORT_LIST:
        if importer_class in importer_classes:
            ordered.append(importer_class)
    return ordered

def _recursively_find_dependencies(importer_class, importer_classes):
    """
    Recursively search for and add the given class's dependencies.

    importer_class: (SQLImporter) The importer class to check for dependencies.
    importer_classes: (list) References to the importer classes to run.
    """
    for dependency in importer_class.DEPENDENCIES:
        # Get the importer class from the table name.
        dependency_class = getattr(importers, 'Importer_%s' % dependency)

        # Protect against infinite recursion.
        if dependency_class not in importer_classes:
            # Add the dependency to the master list of importer classes to run.
            importer_classes.add(dependency_class)
            # Find the dependencies of this dependency.
            _recursively_find_dependencies(dependency_class, importer_classes)

def add_dependencies(importer_classes):
    """
    Given a list of importer classes, add any dependencies needed for a
    complete import of the given tables.
    
    importer_classes: (list) References to the importer classes to run.
    """
    # Make a copy so the Set size doesn't change during iteration.
    original = importer_classes.copy()
    for importer_class in original:
        # Look through all originally requested importers and add
        # their dependencies to the importer list.
        _recursively_find_dependencies(importer_class, importer_classes)
    #print "CLASSES:", importer_classes

def run_importers(importer_classes, include_deps=False):
    """
    importer_classes: (list) References to the importer classes to run.
    """
    # Create the SQLite connection object.
    conn = sqlite3.connect(settings.EVE_CCP_DUMP_SQLITE_DB)
    conn.row_factory = sqlite3.Row

    if include_deps:
        add_dependencies(importer_classes)

    ordered_importers = order_importers(importer_classes)

    # Timestamp of when the imports started.
    time_started = datetime.datetime.now()

    # Carry out the imports in order.
    for importer_class in ordered_importers:
        importer = importer_class()
        importer.prep_and_run_importer(conn)

    # Print the total time, for the ricers.
    time_elapsed = datetime.datetime.now() - time_started
    hours = time_elapsed.seconds / 3600
    minutes = (time_elapsed.seconds % 3600) / 60
    seconds = (time_elapsed.seconds % 3600) % 60
    print "Import completed in %0.2d:%0.2d:%0.2d" % (
        hours, minutes, seconds
    )
