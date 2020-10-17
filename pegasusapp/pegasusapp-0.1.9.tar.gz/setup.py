# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pegasusapp']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.15.18,<2.0.0', 'typer[all]>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['pegasus = pegasusapp.main:app']}

setup_kwargs = {
    'name': 'pegasusapp',
    'version': '0.1.9',
    'description': '',
    'long_description': '# Portal Gun\n\nThe awesome Portal Gun\n',
    'author': 'John Ginger',
    'author_email': 'john@johnginger.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
