# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiocli']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiocli',
    'version': '1.2.1',
    'description': 'Simple and lightweight async console runner.',
    'long_description': "# Async cli client/commander framework\n\naiocli is a Python library for simple and lightweight async console runner.\n\nFull compatibility with argparse module and highly inspired by aiohttp module.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install aiocli.\n\n```bash\npip install aiocli\n```\n\n## Usage\n\n```python\n# examples/commander.py\nfrom aiocli import commander\n\napp = commander.Application()\n\n@app.command(name='greet:to', positionals=[('--name', {'default': 'World!'})])\nasync def handle(args: dict) -> int:\n    print('Hello ' + args.get('name'))\n    return 0\n\nif __name__ == '__main__':\n    commander.run_app(app)\n```\n\n## Requirements\n\n- Python >= 3.6\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://github.com/ticdenis/python-aiocli/blob/master/LICENSE)\n",
    'author': 'ticdenis',
    'author_email': 'denisnavarroalcaide@outlook.es',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ticdenis/python-aiocli',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
