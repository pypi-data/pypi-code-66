# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['MDSimsEval']

package_data = \
{'': ['*']}

install_requires = \
['MDAnalysis>=1.0.0,<2.0.0',
 'imgkit>=1.0.2,<2.0.0',
 'matplotlib>=3.3.2,<4.0.0',
 'mdtraj>=1.9.4,<2.0.0',
 'numpy>=1.19.2,<2.0.0',
 'pandas>=1.0.3,<2.0.0',
 'scikit-learn>=0.23.2,<0.24.0',
 'scipy>=1.5.2,<2.0.0',
 'seaborn>=0.11.0,<0.12.0',
 'tqdm>=4.50.2,<5.0.0']

setup_kwargs = {
    'name': 'mdsimseval',
    'version': '0.1.1',
    'description': 'Collective analysis on a set of Molecular Dynamics simulations.',
    'long_description': '# MD Feature Extraction and Evaluation\n\n**MDSimsEval** is a package we created as part of my undergraduate thesis that in a flexible way calculates useful\nmetrics from a collection of Molecular Dynamics (MD) simulations, stores them and provides a number of methods for\nanalysis and classification.  \n  \nMore specifically the use case we developped this package for was to define and evaluate models used \nfor discriminating agonist vs. antagonist ligands of the 5-HT2A receptor.\n\n**Install**: `pip install mdsimseval`  \n  \n[More can be found on the docs](https://mikexydas.github.io/MDSimsEval/).\n\n## Thesis Abstract\n\nMolecular dynamics (MD) is a computer simulation method for analyzing the physical\nmovements of atoms and molecules. The atoms and molecules are allowed to interact\nfor a fixed period of time, giving a view of the dynamic &quot;evolution&quot; of the system. Then\nthe output of these simulations is analyzed in order to arrive to conclusions depending\non the use case.\n\nIn our use case we were provided with several simulations between ligands and the 5-HT2A \nreceptor which is the main excitatory receptor subtype among the G protein-\ncoupled receptor (GPCRs) for serotonin and a target for many antipsychotic drugs. Our\nsimulations were of two classes. Some of the ligands were agonists meaning that they\nactivated the receptor, while the other were antagonists meaning that they blocked the\nactivation of the receptor.\n\nOur goal was to find a set of features that was able to discriminate agonists from\nantagonists with a degree of certainty. The small discriminative power of the currently\nwell-known descriptors of the simulations motivated us to dig deeper and extract a\ncustom-made feature set. We accomplished that by defining a method which is able to\nfind in a robust way, the residues of the receptor that had the most statistically\nsignificant separability between the two classes.\n',
    'author': 'Mike Xydas',
    'author_email': 'mikexydas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mikexydas.github.io/MDSimsEval/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.9,<4.0.0',
}


setup(**setup_kwargs)
