# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pydev_cli']

package_data = \
{'': ['*']}

install_requires = \
['black>=19.10b0,<20.0',
 'flake8>=3.8.3,<4.0.0',
 'isort>=5.5.1,<6.0.0',
 'mypy>=0.790,<0.791',
 'pre-commit>=2.7.1,<3.0.0',
 'pydantic>=1.6.1,<2.0.0',
 'pytest-cov>=2.10.1,<3.0.0',
 'pytest>=6.0.1,<7.0.0',
 'python-semantic-release>=7.3.0,<8.0.0',
 'toml>=0.10.1,<0.11.0',
 'typer>=0.3.2,<0.4.0']

extras_require = \
{'docs': ['mkdocs>=1.1.2,<2.0.0',
          'mkdocs-material>=6.1.0,<7.0.0',
          'markdown-include>=0.6.0,<0.7.0',
          'mkdocstrings>=0.13.6,<0.14.0']}

entry_points = \
{'console_scripts': ['pydev = pydev_cli.cli:app']}

setup_kwargs = {
    'name': 'pydev-cli',
    'version': '2.0.0',
    'description': 'A single python development dependency to rule them all',
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
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
