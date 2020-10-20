# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['naomilapaglia']

package_data = \
{'': ['*'], 'naomilapaglia': ['static/images/*', 'templates/*']}

entry_points = \
{'console_scripts': ['customize = naomilapaglia.overrides:admin_override']}

setup_kwargs = {
    'name': 'naomilapaglia',
    'version': '0.1.1',
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
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
