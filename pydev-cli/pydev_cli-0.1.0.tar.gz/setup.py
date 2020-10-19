# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pydev_cli']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.6.1,<2.0.0',
 'toml>=0.10.1,<0.11.0',
 'typer>=0.3.2,<0.4.0',
 'uvicorn>=0.12.1,<0.13.0']

entry_points = \
{'console_scripts': ['pydev = pydev_cli.cli:app']}

setup_kwargs = {
    'name': 'pydev-cli',
    'version': '0.1.0',
    'description': 'Useful command line tool to develop in Python',
    'long_description': None,
    'author': 'Guillaume Charbonnier',
    'author_email': 'guillaume.charbonnier@capgemini.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
