# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hass_brightsky_client']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'hass-brightsky-client',
    'version': '0.1.2',
    'description': 'Wrapping the API-specific parts of the brightsky component for Home-Assistant',
    'long_description': None,
    'author': 'Martin Weinelt',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
