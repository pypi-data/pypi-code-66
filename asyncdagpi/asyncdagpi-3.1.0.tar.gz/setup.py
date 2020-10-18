# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncdagpi']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.3,<4.0.0', 'ratelimiter>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'asyncdagpi',
    'version': '3.1.0',
    'description': 'An Asynchronos API wrapper for https://dagpi.xyz',
    'long_description': '# asyncdagpi\n\n[![Build Status](https://travis-ci.com/Daggy1234/asyncdagpi.svg?branch=master)](https://travis-ci.com/Daggy1234/asyncdagpi) [![License](https://img.shields.io/github/license/daggy1234/asyncdagpi)](https://mit-license.org/) ![version](https://img.shields.io/pypi/v/asyncdagpi) ![python](https://img.shields.io/pypi/pyversions/asyncdagpi) [![Documentation Status](https://readthedocs.org/projects/asyncdagpi/badge/?version=latest)](https://asyncdagpi.readthedocs.io/en/latest/?badge=latest)\n\nPowerful Asynchronous Wrapper for dagpi https://dagpi.xyz\n\nInstallation\n----\n\n```shell script\npip install asyncdagpi\n```\n\nData API\n---\n\nSome endpoints like WTP, PickupLine and Logo will return Objects while Waifu will return a Dictionary. Everything else will return a string.\n```python\nfrom asyncdagpi import Client\ndagpi = Client("dagpi token")\n# For WTP Object\nwtp = await dagpi.wtp()\n#For Roast\nroast = await dagpi.roast()\n```\n\nImage Manipulation\n---\nAll Image endpoints return an Image object. This has many properties that can be useful for developers. For Basic implementations are displayed\n\n#### Discord.py\n\n```python\nfrom discord.ext import commands\nimport discord\nfrom asyncdagpi import Client, ImageFeatures\n\nbot = commands.Bot(command_prefix="!")\ndagpi = Client("dagpi token")\n\n@bot.command()\nasync def pixel(ctx, member: discord.Member):\n    url = str(member.avatar_url_as(format="png", static_format="gif", size=1024))\n    img = await dagpi.image_process(ImageFeatures.pixel(), url)\n    file = discord.File(fp=img.image,filename=f"pixel.{img.format}")\n\n```\n\n#### Writing To File\n\n```python\nfrom asyncdagpi import Client, ImageFeatures\ndagpi = Client("dagpi token")\nimg = await dagpi.image_process(ImageFeatures.pixel(), "https://dagbot-is.the-be.st/logo.png")\n#it will auto chose the right format and write to current directory\nimg.write("pixel")\n#will create pixel.png in this case\n```\n#### Python Pillow\n```python\nfrom asyncdagpi import ImageFeatures, Client\nfrom PIL import Image\n\ndagpi = Client("dagpi token")\nimg = await dagpi.image_process(ImageFeatures.pixel(), "https://dagbot-is.the-be.st/logo.png")\nim = Image.open(img.image)\n```\n\n\n### For More Thorough Examples and Feature list read the documentation.\n\n',
    'author': 'Daggy1234',
    'author_email': 'daggy@daggy.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Daggy1234/asyncdagpi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
