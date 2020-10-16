#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='GymBuddy',
      version='1.0',
      description='App to track meals and lifts',
      packages=['gymBuddyApp', 'pages','activityLibrary','users'],
      install_requires= ['asgiref==3.2.10', 'Django==3.1.2', 'django-crispy-forms==1.9.2', 'pytz==2020.1', 'sqlparse==0.3.1', 'Pillow==7.2.0'],
      scripts=['manage.py'],
      entry_point= {
          'console_scripts':
              ['launch_server = manage:main']
      }

     )
