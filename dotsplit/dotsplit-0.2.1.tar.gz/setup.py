# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dotsplit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dotsplit',
    'version': '0.2.1',
    'description': 'Transform dot-delimited strings to an array of python strings.',
    'long_description': "# dotsplit\n> Transform dot-delimited strings to array of python strings.\n```python\n>>> import dotsplit\n>>> dotsplit('group.0.section.a.seat.3')\n['group', '0', 'section', 'a', 'seat', '3']\n```\n\n[![Downloads](https://pepy.tech/badge/dotsplit/month)](https://pepy.tech/project/dotsplit/month)\n[![Supported Versions](https://img.shields.io/pypi/pyversions/dotsplit.svg)](https://pypi.org/project/dotsplit)\n[![Contributors](https://img.shields.io/github/contributors/wilmoore/dotsplit.py.svg)](https://github.com/wilmoore/dotsplit.py/graphs/contributors)\n\n## Installation\n> dotsplit is available on PyPI:\n###### poetry\n```console\n❯ poetry install dotsplit\n```\n###### pip\n```console\n❯ python -m pip install dotsplit\n```\n\n## Testing\n> to run the unit test suite, cd to the root directory and run:\n```\n❯ poetry install\n❯ poetry run pytest\n```\n\n## Licenses\n[![GitHub license](https://img.shields.io/github/license/wilmoore/dotsplit.py.svg)](https://github.com/wilmoore/dotsplit.py/blob/master/license)\n",
    'author': 'Deyon Samuel Washington',
    'author_email': 'winnersonly@realpolyglot.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wilmoore/dotsplit.py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
