# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['basedosdados']

package_data = \
{'': ['*'],
 'basedosdados': ['configs/*',
                  'configs/templates/dataset/*',
                  'configs/templates/table/*']}

install_requires = \
['Jinja2==2.11.2',
 'click==7.1.2',
 'google-cloud-bigquery==1.28.0',
 'google-cloud-storage==1.31.2',
 'pandas-gbq==0.13.2',
 'pyaml==20.4.0',
 'pydata-google-auth==1.1.0',
 'tomlkit==0.7.0']

entry_points = \
{'console_scripts': ['basedosdados = basedosdados.cli:cli']}

setup_kwargs = {
    'name': 'basedosdados',
    'version': '1.1.0a2',
    'description': 'Organizar e facilitar o acesso a dados brasileiros através de tabelas públicas no BigQuery.',
    'long_description': '\n<!-- Header -->\n<p align="center">\n  <a href="https://basedosdados.github.io/mais/">\n    <img src="docs/images/bdmais_logo.png" width="340" alt="Base dos Dados Mais">\n  </a>\n</p>\n\n\n<p align="center">\n    <em>Mecanismo de busca e <b>repositório</b> de bases de dados brasileiras e internacionais.</em>\n</p>\n\n<p align="center">\n  <a href="https://github.com/basedosdados/mais/subscription" target="_blank">\n    <img src="https://img.shields.io/github/watchers/basedosdados/mais.svg?style=social" alt="Watch">\n  </a>\n  <a href="https://github.com/basedosdados/mais/stargazers" target="_blank">\n    <img src="https://img.shields.io/github/stars/basedosdados/mais.svg?style=social" alt="Start">\n  </a>\n  <a href="https://apoia.se/basedosdados" target="_blank">\n    <img src="http://img.shields.io/badge/%E2%9D%A4%20Contribua!%EF%B8%8F%20-%20-ff69b4?style=social" alt="Contribua">\n  </a>\n  </div>\n  <a href="https://twitter.com/intent/tweet?text=Baixe%20e%20faça%20queries%20em%20dados%20publicos,%20tratados%20e%20gratuitos%20com%20a%20Base%20dos%20Dados%20Mais%20🔍%20➕:%20https://basedosdados.github.io/mais/%20via%20@basedosdados" target="_blank">\n    <img src="https://img.shields.io/twitter/url/https/github.com/jonsn0w/hyde.svg?style=social" alt="Tweet">\n  </a>\n</p>\n\n---\n\n## Base dos Dados Mais\n\nUma simples consulta de SQL é o suficiente para cruzamento de bases que\nvocê desejar. Sem precisar procurar, baixar, tratar, comprar um servidor\ne subir clusters.\n\nNosso repositório traz acesso, rapidez, escala, facilidade, economia,\ncuradoria, e transparência ao cenário de dados no Brasil.\n\n\n<p align="center" display="inline-block">\n  <a href="https://console.cloud.google.com/bigquery?p=basedosdados&page=project" target="_blank">\n    <img src="docs/images/bq_button.png" alt="" width="300" display="inline-block" margin="200">\n  </a>\n  <a href="https://basedosdados.github.io/mais" target="_blank" display="inline-block" margin="200">\n    <img src="docs/images/docs_button.png" alt="Start" width="300">\n  </a>\n</p>\n\n## Instale nosso CLI\n\n[![](docs/images/bdd_install.png)](basedosdados.github.io/mais)\n\n\n## Por que o BigQuery?\n\n- **Acesso**: É possível deixar os dados públicos, i.e., qualquer\n  pessoa com uma conta no Google Cloud pode fazer uma query na base,\n  quando quiser.\n- **Rapidez**: Uma query muito longa não demora menos de minutos para\n  ser processada.\n- **Escala**: O BigQuery escala magicamente para hexabytes se necessário.\n- **Facilidade**: Você pode cruzar tabelas tratadas e atualizadas num só lugar.\n- **Economia**: O custo é praticamente zero para usuários - **1\n  TB gratuito por mês para usar como quiser**. Depois disso, são cobrados\n  somente 5 dólares por TB de dados que sua query percorrer.\n\n## Contribua! 💚\n\n**Incentivamos que outras instituições e pessoas contribuam**. Veja mais\ncomo contribuir [aqui](https://basedosdados.github.io/mais/github/).\n\n## Como citar o projeto 📝\n\nO projeto está licenciado sob a [Licença Hipocrática](https://firstdonoharm.dev/version/2/1/license.html). Sempre que usar os dados cite a fonte como:\n\n> Carabetta, J.; Dahis, R.; Israel, F.; Scovino, F. (2020) Base dos Dados Mais: Repositório de Dados. Github - https://github.com/basedosdados/mais.\n\n## Idiomas\n\nDocumentação está em português (quando possível), código e configurações\nestão em inglês.\n\n## Desenvolvimento\n\n#### CLI\n\nSuba o CLI localmente\n\n```sh\nmake create-env\n. .mais/bin/activate\npython setup.py develop\n```\n\n#### Versionamento\n\nPublique nova versão\n\n```sh\npoetry version [patch|minor|major]\npoetry publish --build\n```\n\n#### Docs\nAtualize os docs adicionando ou editando `.md` em `docs/`.\n\nSe for adicionar um arquivo novo, adicione ele em `mkdocs.yml` sob a chave `nav`.\n\nPara testar a documentação, rode:\n\n```sh\nmkdocs serve \n```\n',
    'author': 'Joao Carabetta',
    'author_email': 'joao.carabetta@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/base-dos-dados/bases',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
