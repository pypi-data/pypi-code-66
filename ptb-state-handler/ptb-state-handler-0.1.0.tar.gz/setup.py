# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['state_handler']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.14.0,<0.15.0', 'python-telegram-bot>=12.0']

setup_kwargs = {
    'name': 'ptb-state-handler',
    'version': '0.1.0',
    'description': 'State handler for python-telegram-bot library',
    'long_description': None,
    'author': 'Vlad Pastushenko',
    'author_email': 'iam@vladpi.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
