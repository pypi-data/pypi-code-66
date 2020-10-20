# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ali_sms_api']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6,<3.7', 'pydantic>=1.6,<1.7', 'requests>=2.24,<2.25']

setup_kwargs = {
    'name': 'ali-sms-api',
    'version': '0.1.0',
    'description': '阿里云 短信 SDK',
    'long_description': '# 简介\n\n阿里云短信 SDK [官方文档](https://help.aliyun.com/document_detail/101339.html)\n\n## 注意:\n\n    这个接口仅仅是为了内部使用，虽然您可以获取它的源代码，但是请不要使用在您的项目中.\n    当前我并不对兼容性以及可用性做任何保证。(如果需要使用请联系开发者获取相应的授权)\n',
    'author': 'valbendan',
    'author_email': 'valbendan@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
