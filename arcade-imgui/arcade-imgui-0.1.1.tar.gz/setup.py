# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcade_imgui']

package_data = \
{'': ['*']}

install_requires = \
['arcade>=2.4.3,<3.0.0', 'imgui>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'arcade-imgui',
    'version': '0.1.1',
    'description': 'IMGUI integration for arcade',
    'long_description': '# Arcade ImGui\n\n[The Python Arcade Library](https://arcade.academy/) + [pyimgui](https://github.com/swistakm/pyimgui) = :heart:\n\n:package: [Package](https://pypi.org/project/arcade-imgui/)\n\n## Prerequisite\n\nGet [Poetry](https://python-poetry.org/)\n\n## Clone\n\nClone the repository and change directory\n\n       git clone https://github.com/kfields/arcade-imgui.git\n       cd arcade-imgui\n\n## Run the Demo\n\n        cd imdemo\n        poetry install\n        poetry shell\n        python imdemo\n\n### Individual Examples\n\n        python examples/bullet.py\n        python examples/colors.py\n        etc ...\n\n## Run the ImFlo Demo\n\n        cd imflo\n        poetry install\n        poetry shell\n        python imdemo\n',
    'author': 'Kurtis Fields',
    'author_email': 'kurtisfields@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kfields/arcade-imgui',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
