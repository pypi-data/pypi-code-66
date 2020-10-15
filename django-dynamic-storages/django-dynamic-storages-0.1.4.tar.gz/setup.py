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
 'django-storages[dropbox,google,sftp,azure,boto3,libcloud]>=1.10.1,<2.0.0',
 'django>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'django-dynamic-storages',
    'version': '0.1.4',
    'description': 'A collection of file fields and associated components to allow for dynamic configuration of storage properties for file-based fields within Django models.',
    'long_description': "# Django Dynamic Storages\n\nI'll fill this in with more detail later, but the basic reasoning for this project is that I needed something I could use to extend the already excellent [django-storages](https://github.com/jschneier/django-storages) project such that the storage field on any given `FileField` was a callable I could source a model instance value from. I've also included an abstract class for holding a configuration that stores (securely via [django-fernet-fields](https://github.com/orcasgit/django-fernet-fields)) the access configuration for a given storage backend as well.  \n",
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
