# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphility']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'graphility',
    'version': '0.0.1',
    'description': 'Pure-python NoSQL database.',
    'long_description': 'Graphility pure python, NoSQL, fast database\n============================================\n\nGraphility is based on CodernityDB by `Codernity Labs`_\n\nGraphility is opensource, pure python (no 3rd party dependency), fast (really fast check Speed in documentation if you don\'t believe in words), multiplatform, schema-less, `NoSQL <http://en.wikipedia.org/wiki/NoSQL>`_ database. It has optional support for HTTP server version (Graphility-HTTP), and also Python client library (Graphility-PyClient) that aims to be 100% compatible with embeded version.\n\nYou can call it a more advanced key-value database. With multiple key-values indexes in the same engine. Also Graphility supports functions that are executed inside database.\n\nDocumentation in repo still refers to CodernityDB and will be updated at the end of reconstruction process.\n\nReconstruction\n--------------\n\nAs of 2020 the original CodernityDB has been neglected for quite some time and the original repo has been lost.\n\n`Nick M.`_ already started porting CodernityDB to Python 3. Go to his repo to see progress.\nI\'ll try to backport any changes he makes but I cant\' guarantee anything.\n\nI decided to make my own port because I want to tear it down and rebuild it piece by piece using only Python 3.8+.\nYou know, to fully know the internals. I also want to add graph layer on top of it.\nAlso, Apache 2.0 License requires me to change the name of the project since "CodernityDB"\nis a trademark/servicemark of Codernity_.\n\n\nKey features\n------------\n\n* Native python database\n* Multiple indexes\n* Fast (more than 50 000 insert operations per second see Speed in documentation for details)\n* Embeded mode (default). REST Server and client are planned.\n* Easy way to implement custom Storage\n* Sharding support\n\nInstall\n-------\n\nGraphility is pure Python and does not need external dependencies.\n\n   pip install graphility\n\nor from sources::\n\n   git clone ssh://git@github.com:Gromobrody/graphility.git\n   cd graphility\n   python setup.py install\n\nDevelopment\n-----------\n\nPoetry_ is used as project management tool. After downloading the project, activate the virtual env and install dev dependencies::\n\n    poetry shell\n    poetry install\n\nNow you\'re ready to go.\n\n\nLicense\n-------\n\n* Copyright 2020 Dominik Kozaczko (https://github.com/dekoza)\n* Copyright 2020 Nick M. (https://github.com/nickmasster)\n* Copyright 2011-2013 Codernity (http://codernity.com)\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n\n.. _Codernity Labs: http://labs.codernity.com/codernitydb\n.. _Nick M.: https://github.com/nickmasster\n.. _Poetry: https://python-poetry.org/docs/\n.. _Codernity: https://codernity.com/\n',
    'author': 'Dominik Kozaczko',
    'author_email': 'dominik@kozaczko.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Gromobrody/graphility',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
