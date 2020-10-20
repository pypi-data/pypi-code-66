# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flore', 'flore.libraries']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.3.1,<6.0.0', 'click>=7.1.2,<8.0.0', 'psycopg2-binary>=2.8.6,<3.0.0']

entry_points = \
{'console_scripts': ['flore = flore:flore_cli']}

setup_kwargs = {
    'name': 'flore',
    'version': '0.0.1',
    'description': 'A great option for creating SQL tables in yaml format.',
    'long_description': "![GitHub top language](https://img.shields.io/github/languages/top/marcuxyz/flore-sql) ![GitHub](https://img.shields.io/github/license/marcuxyz/flore-sql) ![GitHub repo size](https://img.shields.io/github/repo-size/marcuxyz/flore-sql)\n\nIt's a script to transform yaml file to SQL-code.\n\nWe worked as a migration to the database. You can create your migration through of migration.yaml file inside migrations folder and run the script for migrate.\n\n# Install\n\nYou can install the script through of pip command:\n\n```bash\npip intall flore-sql\n```\n\n# Usage\n\nRun the command `flore init` to create `migration` folder with the follow files:\n\n- migration.yaml\n- seed.yaml\n- config.yaml\n\n# Configuration\n\nFor configuration the `migration`, open `config.yaml` file and set information:\n\n```yaml\ndialect: 'pg'\nhost: 'localhost'\nport: 5432\nusername: 'postgres'\npassword: 'docker'\ndatabase: 'flore'\n```\n\n`dialect` is a name of the database service, for example: mysql, pg => postgres. Currently support `postgres` only. Now,\nyou can set `username`, `password`, `database`, `port` and `host` for you database.\n\n\n# Migration\n\nFor create migration you set in migration.yaml the following information:\n\n```yaml\ntables:\n  users:\n    name:\n      - varchar:120\n      - required\n    email:\n      - varchar:84\n      - required\n      - unique\n    password:\n      - varchar:255\n    is_admin:\n      - boolean\n      - default false\n  products:\n    price:\n      - float\n```\n\nRun with the follow command\n\n```yaml\nflore run\n```\n\nTo migrate tables your postgres database.",
    'author': 'Marcus Pereira',
    'author_email': 'hi@marcuspereira.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/marcuxyz/flore-sql',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
