import os
from setuptools import setup

# read in README
this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), 'rb') as f:
    long_description = f.read().decode().strip()

# requirements
install_requires = [
    "hop-client >= 0.2",
]
extras_require = {
    'dev': [
        'autopep8',
        'flake8',
        'pytest >= 5.0, < 5.4',
        'pytest-console-scripts',
        'pytest-cov',
    ],
    'docs': [
        'sphinx',
        'sphinx_rtd_theme',
        'sphinxcontrib-programoutput',
    ],
}

setup(
    name = 'hop-plugin-snews',
    description = 'A hop-client plugin for SNEWS.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/SNEWS2/hop-plugin-snews',
    author = 'Patrick Godwin',
    author_email = 'patrick.godwin@psu.edu',
    license = 'BSD 3-Clause',

    packages = ['hop.plugins'],

    entry_points = {'hop_plugin': ["snews-plugin = hop.plugins.snews"]},
    version = '0.0.1',

    python_requires = '>=3.6.*',
    install_requires = install_requires,
    extras_require = extras_require,
    zip_safe = False,

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'License :: OSI Approved :: BSD License',
    ],

)
