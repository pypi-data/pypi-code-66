# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mebula']

package_data = \
{'': ['*']}

extras_require = \
{'azure': ['azure-mgmt-compute>=13.0.0,<14.0.0'],
 'google': ['google-api-python-client>=1.7.11,<2.0.0',
            'lark-parser>=0.9.0,<0.10.0'],
 'oracle': ['oci>=2.10.0,<3.0.0']}

setup_kwargs = {
    'name': 'mebula',
    'version': '0.2.6',
    'description': '',
    'long_description': '.. SPDX-FileCopyrightText: © 2020 Matt Williams <matt@milliams.com>\n   SPDX-License-Identifier: MIT\n\n******\nMebula\n******\n\nMebula is a framework which you can use in your testing code to mock your calls to cloud providers\' APIs.\nAt the moment, Oracle\'s OCI, Google Cloud and Microsoft Azure are supported.\n\nInstallation\n============\n\n- For Microsoft Azure, install the ``mebula[azure]`` package.\n- For Google Cloud, install the ``mebula[google]`` package.\n- For Oracle\'s OCI, install the ``mebula[oracle]`` package.\n\nUsage\n=====\n\nAzure\n-----\n\nYou can use the ``mock_azure`` context manager and then use the Azure functions as normal:\n\n.. code:: python\n\n    from azure.common.client_factory import get_client_from_json_dict\n    from azure.mgmt.compute import ComputeManagementClient\n\n    from mebula.azure import mock_azure\n\n\n    def test_azure():\n        with mock_azure():\n            config_dict = {\n                "clientId": "ad735158-65ca-11e7-ba4d-ecb1d756380e",\n                "clientSecret": "b70bb224-65ca-11e7-810c-ecb1d756380e",\n                "subscriptionId": "bfc42d3a-65ca-11e7-95cf-ecb1d756380e",\n                "tenantId": "c81da1d8-65ca-11e7-b1d1-ecb1d756380e",\n                "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",\n                "resourceManagerEndpointUrl": "https://management.azure.com/",\n                "activeDirectoryGraphResourceId": "https://graph.windows.net/",\n                "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",\n                "galleryEndpointUrl": "https://gallery.azure.com/",\n                "managementEndpointUrl": "https://management.core.windows.net/",\n            }\n            client = get_client_from_json_dict(ComputeManagementClient, config_dict)\n\n            assert list(client.virtual_machines.list("group")) == []\n\nGoogle\n------\n\nYou can use the ``mock_google`` context manager and then use the Google API functions as normal:\n\n.. code:: python\n\n    import googleapiclient.discovery\n\n    from mebula import mock_google\n\n\n    def test_google(client):\n        with mock_google():\n            client = googleapiclient.discovery.build("compute", "v1")\n\n            assert client.instances().list(project="foo", zone="bar").execute() == {}\n\nOracle\n------\n\nYou can use the ``mock_oracle`` context manager and then use the Oracle ``oci`` functions as normal:\n\n.. code:: python\n\n    import oci\n\n    from mebula.oracle import mock_oracle\n\n\n    def test_oracle():\n        with mock_oracle():\n            compute = oci.core.ComputeClient(config={})\n\n            assert compute.list_instances("foo").data == []\n\nCoverage\n========\n\nCoverage is very minimal at the moment. Only launching and listing instances is supported.\n',
    'author': 'Matt Williams',
    'author_email': 'matt@milliams.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/milliams/mebula',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
