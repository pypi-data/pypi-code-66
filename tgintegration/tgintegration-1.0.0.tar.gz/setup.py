# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tgintegration', 'tgintegration.containers', 'tgintegration.utils']

package_data = \
{'': ['*']}

install_requires = \
['pyrogram>=1.0.7,<2.0.0', 'typing-extensions>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'tgintegration',
    'version': '1.0.0',
    'description': 'An Integration Test Library for Telegram Messenger Bots on top of Pyrogram.',
    'long_description': None,
    'author': 'Joscha Götzer',
    'author_email': 'joscha.goetzer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0.0',
}


setup(**setup_kwargs)
