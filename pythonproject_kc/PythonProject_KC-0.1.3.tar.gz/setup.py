import os
import re

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements():
    return [f for f in read('requirements.txt').splitlines() if not f.startswith('#')]


def get_long_description():
    """Transform README.md into a usable long description.
    Replaces relative references to svg images to absolute https references.
    """

    with open('README.md') as f:
        read_me = f.read()

    def replace_relative_with_absolute(match):
        svg_path = match.group(0)[1:-1]
        return ('(https://github.com/google/pybadges/raw/master/'
                '%s?sanitize=true)' % svg_path)

    return re.sub(r'\(tests/golden-images/.*?\.svg\)',
                  replace_relative_with_absolute, read_me)


setup(
    name='PythonProject_KC',                                    # name of the package
    version='0.1.3',                                            # version of this release
    url='https://github.com/kchennen/PythonProject',            # home page for the package
    download_url='https://github.com/kchennen/PythonProject',   # location where the release version may be downloaded
    author='kchennen',                                          # package author’s name
    author_email='author@mail.com',                             # email address of the package author
    description='Python project template',                      # short, summary description of the package
    long_description=read('README.md'),                         # longer description package to build PyPi project page
    license='MIT',                                              # license for the package
    keywords=(                                                  # list of keywords describing the package
        "Python, cookiecutter, unittest, project "
        "templates, example, documentation, tutorial, setup.py, package"
    ),
    install_requires=requirements(),                            # install external packages as dependencies
    packages=['pythonproject'],                                 # same as name
    scripts=['bin/pythonproject'],                              # Runner files to be started from the command line
    entry_points={                                              # Register the main() function of the package
        'console_scripts': ['pythonproject=pythonproject.__main__:main'],
    },
    classifiers=[                                               # list of classifiers to categorize each release
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: X11 Applications',
        'Framework :: Flake8',
        'Framework :: Flask',
        'Framework :: Jupyter',
        'Framework :: Matplotlib',
        'Framework :: Pytest',
        'Framework :: Setuptools Plugin',
        'Framework :: tox',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
