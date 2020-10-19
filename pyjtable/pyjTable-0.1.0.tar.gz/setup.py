# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyjTable']

package_data = \
{'': ['*'], 'pyjTable': ['UNKNOWN.egg-info/*']}

install_requires = \
['SQLAlchemy>=1.3,<2.0']

setup_kwargs = {
    'name': 'pyjtable',
    'version': '0.1.0',
    'description': 'A python+sqlalchemy interface to generate javascript setup for for http://www.jtable.org/ tables.',
    'long_description': None,
    'author': 'Derek Wood',
    'author_email': 'arcann@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
