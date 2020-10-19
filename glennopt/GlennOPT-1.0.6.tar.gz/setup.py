# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['glennopt',
 'glennopt.base_classes',
 'glennopt.helpers',
 'glennopt.nsga3',
 'glennopt.sode']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.3.1,<4.0.0', 'numpy', 'pandas', 'psutil']

setup_kwargs = {
    'name': 'glennopt',
    'version': '1.0.6',
    'description': 'Multi and single objective optimization tool for cfd/computer simulations.',
    'long_description': None,
    'author': 'Paht Juangphanich',
    'author_email': 'paht.juangphanich@nasa.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.9,<4.0.0',
}


setup(**setup_kwargs)
