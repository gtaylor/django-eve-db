#!/usr/bin/env python
from distutils.core import setup
from eve_db import VERSION

LONG_DESCRIPTION = open('README.rst', 'r').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'EVE Online CCP Django ORM database'

setup(name='django-eve_db',
      version=VERSION,
      description="Importers and ORM models for CCP's EVE Online data dump.",
      long_description=LONG_DESCRIPTION,
      author='Gregory Taylor',
      author_email='snagglepants@gmail.com',
      url='https://github.com/gtaylor/django-eve-db',
      packages=[
          'eve_db',
          'eve_db.ccp_importer', 'eve_db.ccp_importer.importers',
          'eve_db.management', 'eve_db.management.commands',
          'eve_db.migrations',
          'eve_db.models'
      ],
      requires=['django', 'django-eve-api'],
      provides=['django-eve-db'],
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
 )
