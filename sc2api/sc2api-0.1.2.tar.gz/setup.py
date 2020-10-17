# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sc2api']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0',
 'asyncpg>=0.21.0,<0.22.0',
 'dnspython>=2.0.0,<3.0.0',
 'motor>=2.3.0,<3.0.0',
 'pymongo>=3.11.0,<4.0.0']

setup_kwargs = {
    'name': 'sc2api',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Tiago Vilela',
    'author_email': 'tiagovla@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
