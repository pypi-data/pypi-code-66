# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mcdbot', 'mcdbot.commands', 'mcdbot.errors']

package_data = \
{'': ['*']}

install_requires = \
['aioredis>=1.3.1,<2.0.0',
 'asyncrcon>=1.1.4,<2.0.0',
 'discord.py>=1.5.0,<2.0.0',
 'loguru>=0.5.3,<0.6.0']

setup_kwargs = {
    'name': 'mcdbot',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jakub Smetana',
    'author_email': 'jakub@smetana.ml',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
