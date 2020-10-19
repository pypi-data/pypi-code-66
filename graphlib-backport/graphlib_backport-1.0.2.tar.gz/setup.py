# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphlib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'graphlib-backport',
    'version': '1.0.2',
    'description': 'Backport of the Python 3.9 graphlib module for Python 3.6+',
    'long_description': "# graphlib backport\n\nBackport of the Python 3.9\n[graphlib](https://docs.python.org/3/library/graphlib.html)\nmodule for older Python versions.\n\n# Supported versions\n\nThis backport currently support Python 3.6, 3.7, 3.8, 3.9 and and pypy3\n(tested with pypy3.6).\n\n\n# Installation\n\n`pip install git+https://github.com/mariushelf/graphlib_backports.git`\n\n# Usage\n\nThe package works the very same way as the original package.\n[Here's](https://docs.python.org/3/library/graphlib.html) the documentation.\n\n\n# Development\n\nThe sourcecode is hosted on\n[github](https://github.com/mariushelf/graphlib_backports).\nTo develop on this package, just clone it, work on it and submit a pull request.\n\n\n## Dev requirements\n\nFor testing against different Python versions, [tox](https://tox.readthedocs.io/en/latest/)\nis required.\n\nTo download the latest original sourcecode into the repository, there is a make target:\n\n`make download_sourcecode`\n\n*Warning*: This overwrites the code in this repo. By default it uses the tag `v3.9.0`,\nbut you can overwrite that with a `tag` environment variable.\n\n\n## Running tests\n\nAs simple as running `tox` on the command line.\n\nThe executables for all python versions must be in the path, e.g,\n`python3.6`, ..., `python3.9`, `pypy3`.\nYou can install them with [pyenv](https://github.com/pyenv/pyenv).\n\n\n## Publishing a new version\n\nUpdate the version in the pyproject.toml and run `make publish` to build and upload\nthe package ti PyPI.\n\n\n# Thanks\n\nI did not create this code -- I only repackaged it so it can be\npip-installed into older versions of Python.\n\nSo all thanks go to the original contributors of the\n[original sourcecode](https://github.com/python/cpython/blob/3.9/Lib/graphlib.py).\n\n\n# Supported versions\n\nThe backport currently supports Python 3.8+. I plan to add support for\nPython 3.7+. This requires some (minimal) work because the original package\nmakes use of the\n[walrus operator](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions).\n\n\n# License\n\n[PSF](https://docs.python.org/3/license.html#psf-license)\n\n",
    'author': 'Marius Helf',
    'author_email': 'helfsmarius@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
