# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nilspodlib']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.2,<2.0.0', 'pandas>=1.1.3,<2.0.0', 'scipy>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'nilspodlib',
    'version': '2.0.0b1',
    'description': 'A Python library to load and convert sensor data recorded by a NilsPod by Portablies.',
    'long_description': None,
    'author': 'Arne Küderle',
    'author_email': 'arne.kuederle@fau.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
