# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tests', 'tooling']

package_data = \
{'': ['*']}

install_requires = \
['click']

entry_points = \
{'console_scripts': ['tooling = tooling.cli:main']}

setup_kwargs = {
    'name': 'tooling',
    'version': '0.1.0',
    'description': 'Top-level package for tooling.',
    'long_description': '=======\ntooling\n=======\n\n\n.. image:: https://img.shields.io/pypi/v/tooling.svg\n        :target: https://pypi.python.org/pypi/tooling\n\n.. image:: https://img.shields.io/travis/SpikingNeuron/tooling.svg\n        :target: https://travis-ci.com/SpikingNeuron/tooling\n\n.. image:: https://readthedocs.org/projects/tooling/badge/?version=latest\n        :target: https://tooling.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\n.. image:: https://pyup.io/repos/github/SpikingNeuron/tooling/shield.svg\n     :target: https://pyup.io/repos/github/SpikingNeuron/tooling/\n     :alt: Updates\n\n\n\nTools for programmers\n\n\n* Free software: BSD-3-Clause\n* Documentation: https://tooling.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `briggySmalls/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage\n',
    'author': 'Praveen Kulkarni',
    'author_email': 'praveenneuron@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SpikingNeuron/tooling',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
}


setup(**setup_kwargs)
