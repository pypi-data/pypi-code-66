# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['doop']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'rotations']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata']}

setup_kwargs = {
    'name': 'doop',
    'version': '0.0.4',
    'description': 'orbital dynamics',
    'long_description': '![](https://raw.githubusercontent.com/nimbus-bp-1729/doop/master/pics/zapp.png)\n\n![Python](https://github.com/nimbus-bp-1729/doop/workflows/Python/badge.svg)\n\n# DOOP\n\n**Still figuring out what I want to do with this**\n\nSome simple python code to do astrodynamics work in python.\n\n- hohman transfers\n- convert between classical orbital parameters and position/velocity in ECI\n- convert between some useful reference frames: \n    - Earth Central Inertial (ECI) [x,y,z]\n    - Earth Centered, Earth Fixed (ECEF) [x,y,z]\n    - North East Down (NED) [x,y,z]\n    - Geocentric [lat,lon,alt]\n\n## Documents\n\n### Two Line Elements ([TLEs](docs/tle/tle.md))\n\n```\nTBD\n```\n\n### Classical Orbital Elements\n\n![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Orbit1.svg/266px-Orbit1.svg.png)\n\n- Semimajor-axis (a)[km]: orbit size\n- Eccentricity (e)[unitless]: orbit shape (0=circule, 1=straight line)\n- Inclination (i)[deg]: orbital plane inclination measure from ascending node\n- Argument of Perigee (w)[deg]: orbit orientation\n- Ascending Node (Omega)[deg]: location of ascending node\n- True Anomaly (v)[deg]: location of satellite in orbit relative to perigee\n- Mean Anomaly (M)[deg]: fictitious angle that varies linearly with time\n\n## Other Useful Packages\n\n- [spaceman3D](https://github.com/Jaseibert/spaceman3D) reading tles, plotting, appears dead, don\'t think it works correctly ... everything has same RAAN\n- [orbital](https://github.com/RazerM/orbital) reading tles, plotting, appears dead\n- [spg4](https://github.com/brandon-rhodes/python-sgp4) propagation, seems ok\n- [tle-tools](https://pypi.org/project/TLE-tools/) not sure value, seems dead\n- [ESA: pykep](https://esa.github.io/pykep/index.html) more for inter-planetary stuff\n- [astrodynamics](https://github.com/dinkelk/astrodynamics) looks good, but it is Matlab code\n- [OrPytal](https://github.com/nicklafarge/OrPytal) does orbits without specific parameters\n\n# References\n\n- [Wiki: Earth parameters](https://en.wikipedia.org/wiki/Earth)\n- [Wiki: Orbital elements](https://en.wikipedia.org/wiki/Orbital_elements)\n- [Wiki: TLE Format](https://en.wikipedia.org/wiki/Two-line_element_set)\n- [celestrak.com TLEs](https://celestrak.com/NORAD/elements/)\n\n# MIT License\n\n**Copyright (c) 2020 Kevin J. Walchko**\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n',
    'author': 'walchko',
    'author_email': 'walchko@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/doop/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
