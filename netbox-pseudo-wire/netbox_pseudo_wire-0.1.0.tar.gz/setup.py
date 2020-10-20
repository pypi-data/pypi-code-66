# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netbox_pseudo_wire',
 'netbox_pseudo_wire.api',
 'netbox_pseudo_wire.migrations']

package_data = \
{'': ['*'],
 'netbox_pseudo_wire': ['templates/netbox_pseudo_wire/*',
                        'templates/netbox_pseudo_wire/inc/*']}

setup_kwargs = {
    'name': 'netbox-pseudo-wire',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Gabri Botha',
    'author_email': 'gabri.botha@bitco.co.za',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
