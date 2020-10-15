# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['data_engineering_extract_metadata']

package_data = \
{'': ['*']}

install_requires = \
['cx_Oracle>=8.0.0,<9.0.0']

setup_kwargs = {
    'name': 'data-engineering-extract-metadata',
    'version': '1.0.0',
    'description': 'A python package for extracting and formatting table metadata from databases',
    'long_description': '# Extract metadata for data engineering pipelines\nThis repo lets you extract metadata from a database and shape it into a folder of json files that [etl_manager](https://github.com/moj-analytical-services/etl_manager) can read. \n\nThe `create_all_metadata` function will do most of the process in one go. See \'quickstart\' below for a summary, or more detailed documentation below that. The end result will be: \n\n- a json file containing a filtered list of tables\n- a subfolder for the metadata\n- in that subfolder, a database.json file with overall metadata for the database\n- also in that subfolder, another .json file listing the columns and other metadata for each table\n\n## Requirements\nThis runs in Python 3.6+. You\'ll need to [install cx_Oracle 8.0.0+](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html). \n\nInstalling cx_Oracle also involves installing its client libraries. You can [download it from Oracle](https://www.oracle.com/database/technologies/instant-client/downloads.html) or, if you\'re on Mac, install by Homebrew:\n\n`brew tap InstantClientTap/instantclient`\n`brew install instantclient-basic`\n\n### cx_Oracle problems 1: client host name\nIf you\'re on a Mac, you might get errors like "cx_Oracle.DatabaseError: ORA-24454: client host name is not set". If you do, you\'ll need to adjust your hosts file. To do this:\n\n- go to system preferences, then sharing, and note the computer name at the top\n- go to your hard disk, then the `etc` folder and find the `hosts` file\n- back up your hosts file in case anything weird happens\n- in hosts, find the line that says `127.0.0.1 localhost`\n- under it, add a new line that says `127.0.0.01 computer_name`, where computer_name is the one you got from system preferences/sharing\n- save the hosts file\n\n### cx_Oracle problems 2: client library location\nDepending on how you installed the Oracle client libraries, the create_oracle_connection function might not work with default parameters. \n\nIf it won\'t connect, try specifying the location of your client libraries using the oracle_client_lib parameter.\n\n## Quick start\nHere\'s an example of creating a full metadata folder by using create_all_metadata and a custom function to filter the table list: \n\n``` python\n\nfrom pathlib import Path\nfrom extract_metadata.connect import create_oracle_connection\nfrom extract_metadata.metadata import create_all_metadata\n\n\ndef table_filter(table_list):\n    """Takes a list of (table, tablespace) tuples and filters it down to tables that have \'REPLICATION_TEST\' in their name"""\n    return [t[0] for t in table_list if "REPLICATION_TEST" in t[0]]\n\n\nsettings_location = Path.cwd().parent / "settings_folder"\nconnection = create_oracle_connection("delius_sandpit", settings_location)\n\ncreate_all_metadata(\n    connection,\n    save_folder="delius",\n    title="delius_sandpit_test",\n    description="Here\'s a description",\n    schema="DELIUS_ANALYTICS_PLATFORM",\n    source_bucket="mojap-raw-hist-dev",\n    source_folder="hmpps/delius/DELIUS_ANALYTICS_PLATFORM",\n    filter_function=table_filter,\n)\n\nconnection.close()\n```\n\nIf you save this in a script called `get_metadata.py` in /metadata/ folder, you\'ll end up with this folder structure: \n\n```\nmetadata\n|-- get_metadata.py\n|-- delius\n|   |-- delius_sandpit_test.json\n|   |-- delius_sandpit_test\n|   |   |-- database.json\n|   |   |-- table1.json\n|   |   |-- table2.json\n```\n\n## Step by step\nThere are 3 steps to getting metadata from a database: \n1. Connect using connect.create_oracle_connection\n2. Make a list of all the tables and filter it to the ones you want - you can do both with table_list.get_table_list\n3. Get metadata from the filtered list of tables using metadata.create_metadata_folder\n\n### 1. Connecting\nYou\'ll need some database connection settings. These should be in a json file structured like this: \n\n``` json\n{\n    "host": "HOST",\n    "password": "PASSWORD",\n    "port": 1234,\n    "service_name": "SERVICE_NAME",\n    "user": "database_username"\n}\n```\n\nThen pass this file and its location to create_oracle_connection in the connect module. You might also need to use the oracle_client_lib parameter to specify where your Oracle client libraries are. See the cx_Oracle connection problems, above. \n\n### 2. Making a list of tables\nget_table_list in the table_list module will use your connection to get a list of tables from the database. \n\nIt will create a timestamped json file listing the tables. Specify the file\'s save_folder and title when you call the function. \n\nAlso specify the database schema to get the tables from.  \n\nYou might not want the file to list all the tables. In this case, pass a filter_function as well. This should be a function that takes a single argument - a list, in this format:\n\n`[("TABLE_NAME", "TABLESPACE"), ("ANOTHER_TABLE_NAME", "TABLESPACE")]`\n\nReturn the tables you want as a list of table names. So if you only wanted the first one from this list, you\'d want to return: \n\n`["TABLE_NAME"]`\n\n### 3. Get the metadata for the tables\nTo read a folder with etl_manager, it must contain a database.json file specifying overall features of the database, plus a json file for each table. \n\nYou can create these in one go using metadata.create_metadata_folder, or separately with metadata.create_json_for_database and metadata.create_json_for_tables.\n\n## Tests\nUnit tests are written for pytest. Run `pytest` from the root folder to start them.\n\nWhere functions involve SQL queries, the unit tests don\'t check these queries - only the Python surrounding them. \n\n## Githooks\nThis repo comes with some githooks to make standard checks before you commit files to Github. The checks are: \n- if you\'re using git-crypt, run `git-crypt status` and check for unencrypted file warnings \n- run Black on Python files\n- run Flake8 on Python files\n- run yamllint on yaml files\n\nIf you want to use these, run this command from the repo\'s root directory: \n\n`git config core.hooksPath githooks`\n\nSee the [data engineering template repo](https://github.com/moj-analytical-services/data-engineering-template) for details. \n\n## Licence\n[MIT Licence](LICENCE.md)\n# Extract metadata for data engineering pipelines\nThis repo lets you extract metadata from a database and shape it into a folder of json files that [etl_manager](https://github.com/moj-analytical-services/etl_manager) can read. \n\nThe `create_all_metadata` function will do most of the process in one go. See \'quickstart\' below for a summary, or more detailed documentation below that. The end result will be: \n\n- a json file containing a filtered list of tables\n- a subfolder for the metadata\n- in that subfolder, a database.json file with overall metadata for the database\n- also in that subfolder, another .json file listing the columns and other metadata for each table\n\n## Requirements\nThis runs in Python 3.6+. You\'ll need to [install cx_Oracle 8.0.0+](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html). \n\nInstalling cx_Oracle also involves installing its client libraries. You can [download it from Oracle](https://www.oracle.com/database/technologies/instant-client/downloads.html) or, if you\'re on Mac, install by Homebrew:\n\n`brew tap InstantClientTap/instantclient`\n`brew install instantclient-basic`\n\n### cx_Oracle problems 1: client host name\nIf you\'re on a Mac, you might get errors like "cx_Oracle.DatabaseError: ORA-24454: client host name is not set". If you do, you\'ll need to adjust your hosts file. To do this:\n\n- go to system preferences, then sharing, and note the computer name at the top\n- go to your hard disk, then the `etc` folder and find the `hosts` file\n- back up your hosts file in case anything weird happens\n- in hosts, find the line that says `127.0.0.1 localhost`\n- under it, add a new line that says `127.0.0.01 computer_name`, where computer_name is the one you got from system preferences/sharing\n- save the hosts file\n\n### cx_Oracle problems 2: client library location\nDepending on how you installed the Oracle client libraries, the create_oracle_connection function might not work with default parameters. \n\nIf it won\'t connect, try specifying the location of your client libraries using the oracle_client_lib parameter.\n\n## Quick start\nHere\'s an example of creating a full metadata folder by using create_all_metadata and a custom function to filter the table list: \n\n``` python\n\nfrom pathlib import Path\nfrom extract_metadata.connect import create_oracle_connection\nfrom extract_metadata.metadata import create_all_metadata\n\n\ndef table_filter(table_list):\n    """Takes a list of (table, tablespace) tuples and filters it down to tables that have \'REPLICATION_TEST\' in their name"""\n    return [t[0] for t in table_list if "REPLICATION_TEST" in t[0]]\n\n\nsettings_location = Path.cwd().parent / "settings_folder"\nconnection = create_oracle_connection("delius_sandpit", settings_location)\n\ncreate_all_metadata(\n    connection,\n    save_folder="delius",\n    title="delius_sandpit_test",\n    description="Here\'s a description",\n    schema="DELIUS_ANALYTICS_PLATFORM",\n    source_bucket="mojap-raw-hist-dev",\n    source_folder="hmpps/delius/DELIUS_ANALYTICS_PLATFORM",\n    filter_function=table_filter,\n)\n\nconnection.close()\n```\n\nIf you save this in a script called `get_metadata.py` in /metadata/ folder, you\'ll end up with this folder structure: \n\n```\nmetadata\n|-- get_metadata.py\n|-- delius\n|   |-- delius_sandpit_test.json\n|   |-- delius_sandpit_test\n|   |   |-- database.json\n|   |   |-- table1.json\n|   |   |-- table2.json\n```\n\n## Step by step\nThere are 3 steps to getting metadata from a database: \n1. Connect using connect.create_oracle_connection\n2. Make a list of all the tables and filter it to the ones you want - you can do both with table_list.get_table_list\n3. Get metadata from the filtered list of tables using metadata.create_metadata_folder\n\n### 1. Connecting\nYou\'ll need some database connection settings. These should be in a json file structured like this: \n\n``` json\n{\n    "host": "HOST",\n    "password": "PASSWORD",\n    "port": 1234,\n    "service_name": "SERVICE_NAME",\n    "user": "database_username"\n}\n```\n\nThen pass this file and its location to create_oracle_connection in the connect module. You might also need to use the oracle_client_lib parameter to specify where your Oracle client libraries are. See the cx_Oracle connection problems, above. \n\n### 2. Making a list of tables\nget_table_list in the table_list module will use your connection to get a list of tables from the database. \n\nIt will create a timestamped json file listing the tables. Specify the file\'s save_folder and title when you call the function. \n\nAlso specify the database schema to get the tables from.  \n\nYou might not want the file to list all the tables. In this case, pass a filter_function as well. This should be a function that takes a single argument - a list, in this format:\n\n`[("TABLE_NAME", "TABLESPACE"), ("ANOTHER_TABLE_NAME", "TABLESPACE")]`\n\nReturn the tables you want as a list of table names. So if you only wanted the first one from this list, you\'d want to return: \n\n`["TABLE_NAME"]`\n\n### 3. Get the metadata for the tables\nTo read a folder with etl_manager, it must contain a database.json file specifying overall features of the database, plus a json file for each table. \n\nYou can create these in one go using metadata.create_metadata_folder, or separately with metadata.create_json_for_database and metadata.create_json_for_tables.\n\n## Tests\nUnit tests are written for pytest. Run `pytest` from the root folder to start them.\n\nWhere functions involve SQL queries, the unit tests don\'t check these queries - only the Python surrounding them. \n\n## How to update\nUpdate and release new versions using Poetry. Make sure to change the version number in `pyproject.toml` and describe the change in `CHANGELOG.md`.\n\nIf you\'ve changed any dependencies in `pyproject.yaml`, run `poetry update` to update `poetry.lock`.\n\nOnce you\'ve created a release in GitHub, to publish the latest version to PyPI, run:\n\n```\npoetry build\npoetry publish -u <username>\n```\n\nHere, you should replace `<username>` with your PyPI username. To publish to PyPI, you must be an owner of the project.\n\n## Licence\n[MIT Licence](LICENCE.md)\n',
    'author': 'Alec Johnson',
    'author_email': 'alec.johnson@digital.justice.gov.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/moj-analytical-services/data-engineering-extract-metadata',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
