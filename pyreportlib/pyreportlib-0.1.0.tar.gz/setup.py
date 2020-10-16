# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyreportlib', 'pyreportlib.utils']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.3.2,<4.0.0',
 'pandas>=1.1.2,<2.0.0',
 'pylatex>=1.4.0,<2.0.0',
 'python-docx>=0.8.10,<0.9.0',
 'xlrd>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'pyreportlib',
    'version': '0.1.0',
    'description': 'pyreportlib is a package for automatic reporting to word and latex',
    'long_description': None,
    'author': 'bernt sørby',
    'author_email': 'bsorby@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/entailor/pyreportlib/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
