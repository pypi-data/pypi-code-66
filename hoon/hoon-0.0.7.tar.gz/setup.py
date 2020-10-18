# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['hoon']
setup_kwargs = {
    'name': 'hoon',
    'version': '0.0.7',
    'description': 'utility functions for DRY develpment',
    'long_description': None,
    'author': 'Pedro Rodrigues',
    'author_email': 'medecau@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
