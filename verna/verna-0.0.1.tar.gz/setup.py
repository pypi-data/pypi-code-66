# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['verna']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'verna',
    'version': '0.0.1',
    'description': 'A module to handle colors',
    'long_description': '# Verna\n\n<a href="https://pypi.org/project/verna"><img alt="PyPI" src="https://img.shields.io/pypi/v/verna"></a>\n<img alt="Build Status" src="https://api.travis-ci.com/ju-sh/verna.svg?branch=master"></img>\n<a href="https://github.com/ju-sh/verna/blob/master/LICENSE.md"><img alt="License: MIT" src="https://img.shields.io/pypi/l/verna"></a>\n\nA simple module to handle colors\n\nOnly RGBA colors are supported at the moment.\n\n---\n\n<h2>Installation</h2>\n\nYou need Python>=3.6 to use Verna.\n\nIt can be installed from PyPI with pip using\n\n    pip install verna\n\n---\n\n<h2>Usage</h2>\n\nColors are represented using objects of class `Color`.\n\nThe color value is essentially stored as an integer as the `integer` attribute.\n\nThe following properties can be used to access the different color components.\n\n    color.alpha\n    color.red\n    color.green\n    color.blue\n\nwhere `color` is an instance of `Color`.\n\nThe different color components can be edited with one of the following values\n\n - a percentage in string form with a \'%\' at the end (eg: "20%")\n - an integer from 0 to 255 (eg: 0xff, 255)\n - a float from 0.0 to 1.0 (only for `alpha` property. eg: 0.4)\n\nSo, the following are valid:\n\n    color = Color(0x00ffff)\n    color.alpha = 0x80\n    color.alpha = "50%"\n    color.alpha = 0.5   # float values can be assigned\n                        # only to alpha property\n\n    color.red = 0xff    # Same as color.red = 255\n    color.red = "100%"\n    color.green = 217\n    color.green = "85%"\n    color.blue = 0xf5\n    color.blue = "96%"\n\nwhereas the following will cause error:\n\n    color = Color(0x00ffff)\n    color.alpha = 0x1ff    # > 0xff\n    color.alpha = -1       # < 0.0\n    color.alpha = "120%"   # > 100%\n    color.alpha = "120"    # No \'%\' at end\n    color.alpha = 1.2      # > 1.0\n    color.alpha = True     # Invalid type: bool\n    color.red = 0.5        # float value accepted only for alpha\n\nA `Color` object may be created in multiple ways.\n\nBy default, alpha value is `0`.\n\n<h6>From integer color code</h6>\n\nFor example, cyan (solid), which has color code `0x00ffff` can be created like\n\n    Color(0x00ffff)\n\nwhich is same as\n\n    Color(65535)\n\n<h6>From color name</h6>\n\n`Color.from_name()` can be used to create `Color` objects from a [CSS3 color name](https://www.w3.org/wiki/CSS3/Color/Extended_color_keywords).\n\nFor example, cyan can be created with\n\n    Color.from_name(\'cyan\')\n\n<h6>From RGBA values</h6>\n\n`Color.from_rgba()` can be used to create an instance of `Color` from RGBA values.\n\n    Color.from_rgba(255, 255, 0)         # solid yellow\n    Color.from_rgba(255, 255, 0, 0.5)    # translucent yellow\n\n',
    'author': 'Julin S',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ju-sh/verna',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
