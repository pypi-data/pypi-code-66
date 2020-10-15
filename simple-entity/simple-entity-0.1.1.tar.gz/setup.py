# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_entity']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.8.1,<3.0.0']

setup_kwargs = {
    'name': 'simple-entity',
    'version': '0.1.1',
    'description': 'Simeple Entity Type for DDD development.',
    'long_description': '# Simple-entity\n\n![CI](https://github.com/duyixian1234/simple-entity/workflows/CI/badge.svg?branch=master)\nSimeple Entity Type for DDD development.\n\n## Install\n\n```bash\npip install -U simple-entity\n```\n\n## Use\n\n```python\nclass Activity(Entity):\n    title: str = "activity"\n    timeCreate: datetime = None\n    timeStart: datetime = None\n    timeEnd: datetime = None\n    timeEdit: datetime = None\n\n    def update(self, fields: List[str]):\n        self.timeEdit = datetime.now()\n        return\n\n\nactivity = Activity(\n        _id="0",\n        title="act0",\n        timeCreate=datetime(2020, 1, 1),\n        timeStart=datetime(2020, 1, 1),\n        timeEnd=datetime(2020, 1, 10),\n    )\nact_dict = {\n    "_id": "0",\n    "timeCreate": datetime(2020, 1, 1, 0, 0),\n    "timeStart": datetime(2020, 1, 1, 0, 0),\n    "timeEdit": None,\n    "timeEnd": datetime(2020, 1, 10, 0, 0),\n    "title": "act0",\n}\n\nassert activity.to_dict() == act_dict\nassert Activity.from_dict(act_dict) == activity\n```\n',
    'author': 'duyixian',
    'author_email': 'duyixian1234@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/duyixian1234/simple-entity',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
