# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrofi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyrofi',
    'version': '0.3.0',
    'description': 'Rofi Menu wrapper for hierarchical menu creation.',
    'long_description': '### About\n\n![PyPI - License](https://img.shields.io/pypi/l/pyrofi.svg)\n![PyPI - Implementation](https://img.shields.io/pypi/implementation/pyrofi.svg)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyrofi.svg)\n![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/astynax/pyrofi.svg)\n[![PyPI](https://img.shields.io/pypi/v/pyrofi.svg)](https://pypi.org/project/pyrofi/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\nPyRofi wraps [Rofi](https://github.com/davatorium/rofi) and helps you to build the hierarchical menus with neat navigation. You can also use te [Wofi](https://hg.sr.ht/~scoopta/wofi) as the "backend".\n\n### Installation\n\nMake sure that you have the Rofi or the Wofi installed. Then just `python3 -m pip install --update --user pyrofi` (requires Python `^3.6`).\n\n### Example\n\n```python\n#!/usr/bin/env python3\n\nfrom pyrofi import run_menu\n\ndef hello_world(_):\n    print(\'Hello World!\')\n\ndef dice():\n    import random\n    return [\'echo\', random.choice(\'123456\')]\n\nrun_menu({\n    \'Calculator\': [\'xcalc\'],\n    \'Games\': {\n        \'Rogue\': [\'rogue\'],\n        \'Angband\': [\'angband\']\n    },\n    \'Calendar\': [\'ncal\', \'2019\'],\n    \'Hello World\': hello_world,\n    \'Dice\': dice,\n})\n```\n\nIf you want to use Wofi, you will need to add `menu_cmd=pyrofi.WOFI_CMD` (or just `menu_cmd=\'wofi`) to the `run_menu` call.\n\nMore complex example you can see [here](https://github.com/astynax/pyrofi/blob/master/pyrofi/__main__.py) and run it with `python3 -m pyrofi`.\n',
    'author': 'Aleksei Pirogov',
    'author_email': 'astynax@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/astynax/pyrofi',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
