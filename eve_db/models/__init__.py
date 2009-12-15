"""
By importing all of these sub-modules, the models package is transparently
accessible by the rest of the project. This makes it act just as if it were
one monolithic models.py.
"""
from core import *
from inventory import *
from map import *
from eve_db.models import *
from chr import *
from npc import *
from station import *