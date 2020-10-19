# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sro2syllabics']

package_data = \
{'': ['*']}

install_requires = \
['cree-sro-syllabics>=2020.6.23,<2021.0.0']

entry_points = \
{'console_scripts': ['sro2syllabics = sro2syllabics:sro2syllabics_main']}

setup_kwargs = {
    'name': 'sro2syllabics',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Eddie Antonio Santos',
    'author_email': 'easantos@ualberta.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
