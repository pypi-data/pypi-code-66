# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['cognite',
 'cognite.airworkflow',
 'cognite.airworkflow.model',
 'cognite.airworkflow.util']

package_data = \
{'': ['*'], 'cognite.airworkflow': ['schemas/*']}

install_requires = \
['PyGithub>=1.51,<2.0',
 'bandit>=1.6.2,<2.0.0',
 'black>=19.10b0,<20.0',
 'cerberus>=1.3.2,<2.0.0',
 'cognite-air-ds-util',
 'cognite-air-sdk>=2,<3',
 'cognite-sdk-experimental>=0,<1',
 'cognite-sdk>=2,<3',
 'croniter>=0.3.31,<0.4.0',
 'firebase-admin>=4.3.0,<5.0.0',
 'gitpython>=3.1.1,<4.0.0',
 'isort>=4.3.21,<5.0.0',
 'jinja2>=2.11.2,<3.0.0',
 'pre-commit>=2.7.1,<3.0.0',
 'pyjwt>=1.7.1,<2.0.0',
 'pytest-cov>=2.8.1,<3.0.0',
 'pytest-custom_exit_code>=0.3.0,<0.4.0',
 'pytest>=5.4.2,<6.0.0',
 'ruamel.yaml>=0.16.10,<0.17.0',
 'ruptures>=1.0.3,<2.0.0',
 'scikit-learn>=0.23.1,<0.24.0',
 'sendgrid==6.3.1',
 'slackclient>=2.7.2,<3.0.0',
 'statsmodels>=0.11.1,<0.12.0',
 'toolz>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'cognite-air-workflow',
    'version': '1.0.0',
    'description': 'Client library to perform all required cognite airflow functions built to function with AIR CDF',
    'long_description': None,
    'author': 'Arun Kaashyap Arunachalam',
    'author_email': 'arun.arunachalam@cognite.com',
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
