# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vizel']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.1,<8.0.0', 'graphviz>=0.13.2,<0.14.0', 'six>=1.14.0,<2.0.0']

extras_require = \
{':python_version >= "2.7" and python_version < "3.0"': ['networkx==2.2'],
 ':python_version >= "3.5" and python_version < "4.0"': ['networkx==2.4']}

entry_points = \
{'console_scripts': ['vizel = vizel.cli:main']}

setup_kwargs = {
    'name': 'vizel',
    'version': '0.3.0',
    'description': 'Vizualise a Zettelkasten',
    'long_description': "![Vizel](assets/vizel_banner@2x.jpg)\n\n[![Build Status](https://travis-ci.com/BasilPH/vizel.svg?branch=master)](https://travis-ci.com/BasilPH/vizel)\n\nSee the stats and connections of your Zettelkasten.\n\n![Demo](assets/vizel_demo.gif)\n\n## Getting Started\n\n### Required Zettelkasten structure\n\nVizel tries to be format agnostic without requiring configuration.\n\nVizel makes the following assumptions:\n\n* The Zettel files have an `.md` or `.txt` extension.\n* All Zettel are in one single directory.\n* References use the `[[REFERENCE]]` or `[LABEL](REFERENCE)` format.\n* References of a Zettel pointing to itself are ignored.\n\nVizel was first developed for the format used by the\n[The Archive](https://zettelkasten.de/the-archive/). Other formats are\nnow supported as well, thanks to the help from the community.\n\n### Installing\n\nRun `pip install vizel`\n\nIf you get an error about missing graphviz when running the `graph-pdf`\ncommand, you might need to install it with\n\n` brew install graphviz` on OS X or\n\n`sudo apt-get install graphviz` on Ubuntu.\n\n## Usage\n\n`vizel` has the following commands:\n\n#### graph-pdf\n\n```\nvizel graph-pdf [OPTIONS] DIRECTORY\n\nGenerates a PDF displaying the graph created spanned by Zettel and their connections in the folder DIRECTORY.\n\nOptions:\n  --pdf-name TEXT  Name of the PDF file the graph is written into. Default:\n                   vizel_graph\n  --help  Show this message and exit.\n```\n\n#### stats\n\n```\n\nUsage: vizel stats [OPTIONS] DIRECTORY\n\n  Prints the stats of the graph spanned by Zettel in DIRECTORY.\n\n  Stats calculated:\n  - Number of Zettel\n  - Number of references between Zettel (including bi-directional and duplicate)\n  - Number of Zettel without any reference from or to a Zettel\n  - Number of connected components\n  \nOptions:\n  --help  Show this message and exit.\n```\n\n##### A note on connected components\n\nThe fewer connected components your Zettelkasten has, the better. The\nideal number is 1. It means that you can reach any Zettel by following\nlinks. This, in turn, should increase the likelihood of making new\nsemantic connections.\n\nConnected components are a concept from graph theory. In the context of\na Zettelkasten and vizel, a connected component is a set of Zettel,\nwhich can be reached from any other Zettel in the same component by\nfollowing links. Those links do not need to be direct but can pass\nthrough other Zettel. The direction of the links also doesn't matter.\n\nTwo Zettel are not in the same component if there is no way to reach one\nfrom the other through links.\n\nConnected components will show up as separate clusters of Zettel when\nusing `graph-pdf`. Use the `components` command to get a list of your\ncomponents, and the Zettel contained in each.\n\n#### unconnected\n\n```\nUsage: vizel unconnected [OPTIONS] DIRECTORY\n\n  Prints all of the Zettel in DIRECTORY that have no in- or outgoing\n  references.\n\nOptions:\n  --help  Show this message and exit.\n```\n\n#### components\n\n```\nUsage: vizel components [OPTIONS] DIRECTORY\n\n  Lists the connected components and their Zettel in DIRECTORY.\n\nOptions:\n  --help  Show this message and exit.\n```\n\n## Built With\n\n* [NetworkX](https://networkx.github.io/): Network analysis in Python\n* [click](https://click.palletsprojects.com): Python composable\n  command-line interface toolkit\n* [Graphviz](https://github.com/xflr6/graphviz): Simple Python interface\n  for Graphviz\n\n## Updates & Contributing\n\nFeel free to open issues and pull-requests. Subscribe to the\n[vizel newsletter](https://tinyletter.com/vizel) to be informed about\nnew releases and features in development.\n\nYou can reach out to me for feedback or questions on\n[Twitter](https://twitter.com/BasilPH) or through\n[my website](https://interdimensional-television.com/).\n\nIf you've found vizel useful, please consider\n[sponsoring](https://github.com/sponsors/BasilPH) maintenance and\nfurther development. Or\n[buying me a coffee](https://www.buymeacoffee.com/interdimension).\n\n\n### Development install\n\nThe project uses [Poetry](https://python-poetry.org/).\n\n1. Install Poetry.\n2. Clone this repository.\n3. Run `poetry install` in the root of this project.\n\n### Running tests\n\nRun `py.test` in the `tests` directory.\n\n\n## Versioning\n\nVizel uses [SemVer](http://semver.org/) for versioning. For the versions\navailable, see the\n[tags on the repository](https://github.com/BasilPH/vizel/tags).\n\n## Authors\n\n* **Basil Philipp** - *Owner*\n\n## License\n\nThis project is licensed under GNU GPLv3.\n\n## Acknowledgments\n\n* Thank you Christian Tietze and Sascha Fast for creating\n  [The Archive](https://zettelkasten.de/the-archive/) app and writing a\n  [book](https://zettelkasten.de/book/de/) (German only) on the\n  Zettelkasten method.\n\n",
    'author': 'Basil Philipp',
    'author_email': 'basil@interdimensional-television.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BasilPH/vizel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
