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
    'version': '0.6.0',
    'description': 'Time Series Generator',
    'long_description': '# tsgen\n\n[![CI/CD Status](https://github.com/MarwanDebbiche/tsgen/workflows/CI%2FCD/badge.svg?branch=master)](https://github.com/MarwanDebbiche/tsgen/actions?query=branch:master)\n[![Coverage Status](https://coveralls.io/repos/github/MarwanDebbiche/tsgen/badge.svg?branch=master)](https://coveralls.io/github/MarwanDebbiche/tsgen?branch=master)\n[![Latest Version](https://img.shields.io/pypi/v/tsgen.svg?color=blue)](https://pypi.python.org/pypi/tsgen)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/tsgen?label=pypi%20downloads)](https://pypi.org/project/tsgen/)\n![License](https://img.shields.io/github/license/MarwanDebbiche/tsgen)\n\ntsgen (for Time Series Generator) is a package developed for educational purposes that helps create unidimensional time series of different shapes.\n\n## Installation\n\nYou can install tsgen from PyPI using pip:\n\n```\npip install tsgen\n```\n\n## Getting started\n\n![Getting Started](https://raw.githubusercontent.com/MarwanDebbiche/tsgen/master/images/getting_started.png)\n\nSee the [documentation](https://tsgen.readthedocs.io/en/stable/index.html) for more details.\n',
    'author': 'Marwan Debbiche',
    'author_email': 'marwan.debbiche@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MarwanDebbiche/tsgen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
