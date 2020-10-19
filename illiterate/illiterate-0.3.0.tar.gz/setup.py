# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['illiterate']

package_data = \
{'': ['*']}

install_requires = \
['tqdm>=4.49.0,<5.0.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['illiterate = illiterate.cli:app']}

setup_kwargs = {
    'name': 'illiterate',
    'version': '0.3.0',
    'description': 'Unobstrusive literate programming experience for Python pragmatists',
    'long_description': None,
    'author': 'Alejandro Piad',
    'author_email': 'alepiad@gmail.com',
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
