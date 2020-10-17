# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trashpy']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=1.12.3,<2.0.0',
 'google-auth-oauthlib>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['trashpy = trashpy.main:main']}

setup_kwargs = {
    'name': 'trashpy',
    'version': '1.0.2',
    'description': '',
    'long_description': None,
    'author': 'Paul Bailey',
    'author_email': 'paul.m.bailey@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
