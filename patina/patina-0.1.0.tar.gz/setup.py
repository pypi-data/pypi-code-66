# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['patina']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'patina',
    'version': '0.1.0',
    'description': 'Result and Option types for Python',
    'long_description': None,
    'author': 'Patrick Gingras',
    'author_email': '775.pg.12@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
