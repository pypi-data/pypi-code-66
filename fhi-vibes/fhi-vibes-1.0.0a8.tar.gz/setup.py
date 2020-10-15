# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vibes',
 'vibes.ase',
 'vibes.ase.db',
 'vibes.ase.md',
 'vibes.calculator',
 'vibes.cli',
 'vibes.cli.scripts',
 'vibes.cli.scripts.run',
 'vibes.fireworks',
 'vibes.fireworks.cli',
 'vibes.fireworks.tasks',
 'vibes.fireworks.tasks.fw_out',
 'vibes.fireworks.tasks.postprocess',
 'vibes.fireworks.utils',
 'vibes.fireworks.workflows',
 'vibes.green_kubo',
 'vibes.harmonic_analysis',
 'vibes.helpers',
 'vibes.helpers.supercell',
 'vibes.hiphive',
 'vibes.k_grid',
 'vibes.konstanten',
 'vibes.materials_fp',
 'vibes.molecular_dynamics',
 'vibes.phono3py',
 'vibes.phonopy',
 'vibes.relaxation',
 'vibes.slurm',
 'vibes.spglib',
 'vibes.structure',
 'vibes.tasks',
 'vibes.tdep',
 'vibes.templates',
 'vibes.templates.config_files',
 'vibes.templates.settings',
 'vibes.trajectory']

package_data = \
{'': ['*']}

install_requires = \
['ase>=3.19.0,<4.0.0',
 'attrs>=19.1,<20.0',
 'click>=7.1,<8.0',
 'click_aliases>=1.0,<2.0',
 'click_completion>=0.5.2,<0.6.0',
 'jconfigparser>=0.1.2,<0.2.0',
 'jinja2>=2.10,<3.0',
 'matplotlib>=3.1,<4.0',
 'netCDF4>=1.5,<2.0',
 'numpy>=1.11,<2.0',
 'pandas>=1.0,<2.0',
 'phonopy>=2.6,<2.7.0',
 'scipy>=1.1.1,<2.0.0',
 'seekpath>=1.8.4,<2.0.0',
 'son>=0.3.2,<0.4.0',
 'spglib>=1.12,<2.0',
 'tables>=3.5,<4.0',
 'xarray>=0.12,<0.13']

extras_require = \
{'fireworks': ['fireworks>=1.9,<2.0',
               'python-gssapi>=0.6.4,<0.7.0',
               'pymongo>=3.8,<4.0',
               'fabric>=2.4,<3.0',
               'paramiko>=2.4,<3.0'],
 'hiphive': ['hiphive>=0.5.0,<0.6.0'],
 'phono3py': ['phono3py>=1.19,<2.0'],
 'postgresql': ['psycopg2>=2.8.0,<3.0.0']}

entry_points = \
{'console_scripts': ['vibes = vibes.cli:cli']}

setup_kwargs = {
    'name': 'fhi-vibes',
    'version': '1.0.0a8',
    'description': 'Fritz Haber Institute Vibrational Simulations',
    'long_description': 'FHI-vibes\n===\n\nWelcome to `FHI-vibes`, a `python` package for calculating, analyzing, and understanding the vibrational properties of anharmonic solids from first principles. `FHI-vibes` is intended to bridge between different methodologies, so to allow for a seamless assessment of vibrational properties with different approaches, ranging from the harmonic approximation to anharmonic MD. `FHI-vibes` builds on several [existing packages](https://vibes-developers.gitlab.io/vibes/Credits/) and interfaces them in a consistent and user-friendly fashion. \n\nIts main features are:\n\n- Geometry optimization via [ASE](https://wiki.fysik.dtu.dk/ase/ase/optimize.html#module-ase.optimize),\n- harmonic phonon calculations via [Phonopy](https://atztogo.github.io/phonopy/),\n- molecular dynamics simulations in [NVE](https://wiki.fysik.dtu.dk/ase/ase/md.html#constant-nve-simulations-the-microcanonical-ensemble), [NVT](https://wiki.fysik.dtu.dk/ase/ase/md.html#module-ase.md.langevin), and [NPT](https://wiki.fysik.dtu.dk/ase/ase/md.html#module-ase.md.nptberendsen) ensembles,\n- [harmonic sampling](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.96.115504), and\n- [anharmonicity quantification](https://arxiv.org/abs/2006.14672).\n\nMost of the functionality is high-throughput ready via [fireworks](https://materialsproject.github.io/fireworks/#).\n\n## Overview\n\n- [Installation](https://vibes-developers.gitlab.io/vibes/Installation/)\n- [Tutorial](https://vibes-developers.gitlab.io/vibes/Tutorial/0_intro/)\n- [Documentation](https://vibes-developers.gitlab.io/vibes/Documentation/0_intro/)\n- [Credits](https://vibes-developers.gitlab.io/vibes/Credits/)\n- [References](https://vibes-developers.gitlab.io/vibes/References/)\n\n\n\n## News\n\n- [the best is yet to come](https://www.youtube.com/watch?v=B-Jq26BCwDs)',
    'author': 'Florian Knoop',
    'author_email': 'knoop@fhi-berlin.mpg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/vibes-developers/vibes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
