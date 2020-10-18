# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emmett_haml']

package_data = \
{'': ['*']}

install_requires = \
['emmett>=2,<3', 'renoir-haml>=1.0,<2.0']

setup_kwargs = {
    'name': 'emmett-haml',
    'version': '1.0.0',
    'description': 'HAML syntax for Emmett templates',
    'long_description': '# Emmett-HAML\n\nEmmett-HAML is an [Emmett framework](https://github.com/emmett-framework/emmett) extension providing an HAML like syntax for templates. This is not a template engine but a compiler which converts HAML files to HTML Renoir templates.\n\n[![pip version](https://img.shields.io/pypi/v/emmett-haml.svg?style=flat)](https://pypi.python.org/pypi/emmett-haml)\n\n## Installation\n\nYou can install Emmett-HAML using pip:\n\n    pip install emmett-haml\n\nAnd add it to your Emmett application:\n\n```python\nfrom emmett_haml import Haml\n\napp.use_extension(Haml)\n```\n\n## License\n\nEmmett-HAML is released under BSD license. Check the LICENSE file for more details.\n',
    'author': 'Giovanni Barillari',
    'author_email': 'gi0baro@d4net.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gi0baro/emmett-haml',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
