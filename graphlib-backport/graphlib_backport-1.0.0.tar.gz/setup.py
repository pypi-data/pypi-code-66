# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphlib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'graphlib-backport',
    'version': '1.0.0',
    'description': 'Backport of the Python 3.9 graphlib module for Python 3.6+',
    'long_description': None,
    'author': 'Marius Helf',
    'author_email': 'helfsmarius@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
