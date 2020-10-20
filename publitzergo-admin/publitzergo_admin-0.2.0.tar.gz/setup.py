# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['publitzergo_admin']

package_data = \
{'': ['*'], 'publitzergo_admin': ['static/images/*', 'templates/*']}

entry_points = \
{'console_scripts': ['customize = publitzergo_admin.overrides:admin_override']}

setup_kwargs = {
    'name': 'publitzergo-admin',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'drazum',
    'author_email': 'domagoj.razum1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
