from os import path
from setuptools import setup, find_packages
import sys
import versioneer


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 6)
if sys.version_info < min_version:
    error = """
gunc does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*(sys.version_info[:2] + min_version))
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='gunc',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Python package for detection of chimerism and contamination in prokaryotic genomes.",
    long_description=readme,
    author="Anthony Fullam",
    author_email='anthony.fullam@embl.de',
    url='https://github.com/grp-bork/gunc',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            "gunc = gunc.gunc:main",
        ],
    },
    include_package_data=True,
    package_data={
        'gunc': [
            'data/genome2taxonomy_ref.tsv',
            'tests/test_data/*'
        ]
    },
    install_requires=requirements,
    license="BSD (3-clause)",
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ],
)
