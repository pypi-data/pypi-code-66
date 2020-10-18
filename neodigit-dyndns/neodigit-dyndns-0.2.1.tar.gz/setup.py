# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neodigit_dyndns']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'neodigit-dyndns',
    'version': '0.2.1',
    'description': "A dynamic DNS client using Neodigit's API",
    'long_description': None,
    'author': 'Eduardo Collado',
    'author_email': 'edu@tecnocratica.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
