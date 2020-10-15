# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dynamic_storages',
 'dynamic_storages.db',
 'dynamic_storages.migrations',
 'dynamic_storages.models',
 'dynamic_storages.tasks',
 'dynamic_storages.tests',
 'dynamic_storages.tests.migrations']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.0.0,<9.0.0',
 'django-fernet-fields>=0.6,<0.7',
 'django-storages[libcloud,sftp,dropbox,boto3,google,azure]>=1.10.1,<2.0.0',
 'django>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'django-dynamic-storages',
    'version': '0.1.1',
    'description': 'A collection of file fields and associated components to allow for dynamic configuration of storage properties for file-based fields within Django models.',
    'long_description': None,
    'author': 'Patrick McClory',
    'author_email': 'patrick@mcclory.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mcclory/django-dynamic-storages',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
