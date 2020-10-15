# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tsgen']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=5.3,<6.0', 'numpy>=1.19.2,<2.0.0', 'pandas>=1.1.3,<2.0.0']

setup_kwargs = {
    'name': 'tsgen',
    'version': '0.1.0',
    'description': 'Time Series Generator',
    'long_description': None,
    'author': 'Marwan Debbiche',
    'author_email': 'marwan.debbiche@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
