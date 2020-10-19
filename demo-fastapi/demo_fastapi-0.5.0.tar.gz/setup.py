# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['demo_fastapi', 'demo_fastapi.logging', 'demo_fastapi.tracing']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.61.1,<0.62.0',
 'jaeger-client>=4.3.0,<5.0.0',
 'loguru>=0.5.3,<0.6.0',
 'opentracing>=2.3.0,<3.0.0',
 'typer>=0.3.2,<0.4.0',
 'uvicorn>=0.12.1,<0.13.0']

setup_kwargs = {
    'name': 'demo-fastapi',
    'version': '0.5.0',
    'description': 'Demonstration Rest API built using fastapi',
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
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
