# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aireport', 'aireport.build.lib.tools', 'aireport.tools']

package_data = \
{'': ['*'], 'aireport': ['aireport.egg-info/*', 'dist/*']}

install_requires = \
['aihelper>=0.2.5,<0.3.0',
 'black>=19.10b0,<20.0',
 'numpy',
 'pandas>=1.0.5,<2.0.0']

setup_kwargs = {
    'name': 'aireport',
    'version': '0.1.8',
    'description': '',
    'long_description': None,
    'author': 'None',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
