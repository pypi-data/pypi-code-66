# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fastrepo',
 'fastrepo.templates.default.hooks',
 'fastrepo.templates.default.{{cookiecutter.project_slug}}.src.{{cookiecutter.project_slug}}',
 'fastrepo.templates.default.{{cookiecutter.project_slug}}.tests']

package_data = \
{'': ['*'],
 'fastrepo': ['templates/default/*',
              'templates/default/{{cookiecutter.project_slug}}/*',
              'templates/default/{{cookiecutter.project_slug}}/.azuredevops/pull_request_template/*',
              'templates/default/{{cookiecutter.project_slug}}/.gitlab/merge_request_templates/*',
              'templates/default/{{cookiecutter.project_slug}}/.vscode/*',
              'templates/default/{{cookiecutter.project_slug}}/ci/*',
              'templates/default/{{cookiecutter.project_slug}}/docs/*',
              'templates/default/{{cookiecutter.project_slug}}/docs/apidoc/*',
              'templates/default/{{cookiecutter.project_slug}}/notebooks/*']}

install_requires = \
['cookiecutter>=1.7.2,<2.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['fastrepo = fastrepo:app']}

setup_kwargs = {
    'name': 'fastrepo',
    'version': '1.3.1',
    'description': '',
    'long_description': None,
    'author': 'gcharbon',
    'author_email': 'guillaume.charbonnier@capgemini.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
