# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ckan_editor_utils']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.15.16,<2.0.0', 'requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'ckan-editor-utils',
    'version': '0.1.4',
    'description': 'Utilities for editing CKAN using its API.',
    'long_description': '## Introduction\nThis library assists CKAN editors with doing batch edits and pairs well with a library like pandas.\n\n## Installation\n```shell script\npip install ckan-editor-utils\n```\nThe `requests` package is used for all the underlying API calls.  \nThe `boto3` AWS SDK package is used for accessing and uploading files from S3. \n\n## Usage\n```python\nimport ckan_editor_utils\n```\n### Simple API commands\nFor the basic API commands, much of the `requests` boilerplate code is done for you. \nHowever, the URL must already have a suffix like `/api/action/`.\n```python\nurl = \'https://horizon.uat.gsq.digital/api/action/\'\napi_key = os.environ.get(\'CKAN_API_KEY\')\ndataset_id = \'my-test-dataset\'\n\nres_create = ckan_editor_utils.package_create(url, \n                                           api_key, \n                                           {\n                                               \'name\': dataset_id,\n                                               \'extra:identifier\': dataset_id,\n                                               \'notes\': \'my description\',\n                                               \'owner_org\': \'geological-survey-of-queensland\',\n                                           })\nres_create\n# <Response [200]>\n# This requests response can be viewed by using the .text or .json() methods\nres_create.json()\n# {"help": "https://uat-external.dnrme-qld.links.com.au/api/3/action/help_show?name=package_create", "success": true, "result": {...\n```\nThe response text shows the entire package as CKAN has recorded it. It will populate additional items like \nthe Organisation description automatically. \nAlways check the HTTP status before interacting with the data payload. A 409 will be received if it already exists or if\nwe did not provide enough information for the type of dataset we want to be created, among other reasons. \n\nWe can use `package_show` to get the metadata for an existing dataset:\n```python\nres_show = ckan_editor_utils.package_show(url, api_key, dataset_id)\nres_show.json()\n# {\'help\': \'https://uat-external.dnrme-qld.links.com.au/api/3/action/help_show?name=package_show\', \'success\': True, \'result\': {\'extra:theme\': []...\n```\n\nMore examples of basic API usage can be found [at the Open Data API page by GSQ.](https://github.com/geological-survey-of-queensland/open-data-api#using-python)\n\n### Simplified CKAN Responses\nWhen interacting with the CKAN API, it can be difficult to get a consistent result. Some errors are text not JSON, and \nthe JSON errors sometimes contain different attributes depending on the context.\nManaging the variety of these responses means a lot of extra logic is needed, which clutters up your script.\n\nThis library offers a new `CKANReponse` object that can convert `requests` responses from CKAN into something \nmore consistent and manageable. To use it, simply pass it a CKAN response you received when using `requests`.\n```python\ncheck_res_show = ckan_editor_utils.CKANResponse(res_show)  # (response from earlier example)\nprint(check_res_show)\n# Response 200 OK\ncheck_res_show.ok\n# True\ncheck_res_show.result\n# {\'extra:theme\': [], \'license_title\': None, \'maintainer\': None, ...\n``` \nA JSON response will always be present in the `result` attribute of the CKAN response.\nThis means you can reliably use `result` to capture output and it will always be relevant.\nFurthermore the API action made will be logged to stdout/the console, so you can easily track progress. \n\n\n\n### Managed API actions\nSome common workflows have been developed and make it easier to do simple actions.\nAs an editor doing bulk changes, you might not be sure if every package already exists before you can safely \ncall `package_update()`. Instead, you can just call `put_dataset()`, and the managed session will either create or \nupdate the dataset depending on what it finds.\n\nThe following managed actions are available via the `CKANEditorSession` context manager class:\n* put_dataset (create or update)\n* delete_dataset (delete and purge)\n* put_resource_from_s3 (automatically does multipart uploads)\n\nAdditionally, the `CKANEditorSession` will fix up any URLs that are missing the required extensions.\n\n```python\nwith ckan_editor_utils.CKANEditorSession(url, api_key) as ckaneu:\n    return ckaneu.delete_dataset(dataset_id).result\n```\n',
    'author': 'Eric McCowan',
    'author_email': 'eric.mccowan@servian.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
