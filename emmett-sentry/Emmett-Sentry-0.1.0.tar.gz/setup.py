# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emmett_sentry']

package_data = \
{'': ['*']}

install_requires = \
['emmett>=2.1.0', 'sentry-sdk>=0.17.1']

setup_kwargs = {
    'name': 'emmett-sentry',
    'version': '0.1.0',
    'description': 'Sentry extension for Emmett framework',
    'long_description': '# Emmett-Sentry\n\nEmmett-Sentry is an [Emmett framework](https://emmett.sh) extension integrating [Sentry](https://sentry.io) monitoring platform.\n\n[![pip version](https://img.shields.io/pypi/v/emmett-sentry.svg?style=flat)](https://pypi.python.org/pypi/emmett-sentry) \n\n## Installation\n\nYou can install Emmett-Sentry using pip:\n\n    pip install emmett-sentry\n\nAnd add it to your Emmett application:\n\n```python\nfrom emmett_sentry import Sentry\n\nsentry = app.use_extension(Sentry)\n```\n\n## Configuration\n\nHere is the complete list of parameters of the extension configuration:\n\n| param | default | description |\n| --- | --- | --- |\n| dsn | | Sentry project\'s DSN |\n| environment | development | Application environment |\n| release | | Application release |\n| auto\\_load | `True` | Automatically inject extension on routes |\n| enable\\_tracing | `False` | Enable tracing on routes |\n\n## Usage\n\nThe extension exposes two methods to manually track events:\n\n- exception\n- message\n\nYou call these methods directly within your code:\n\n```python\n# track an error\ntry:\n    1 / 0\nexcept Exception:\n    sentry.exception()\n\n# track a message\nsentry.message("some event", level="info")\n```\n\n## License\n\nEmmett-Sentry is released under BSD license.\n',
    'author': 'Giovanni Barillari',
    'author_email': 'gi0baro@d4net.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/emmett-framework/sentry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
