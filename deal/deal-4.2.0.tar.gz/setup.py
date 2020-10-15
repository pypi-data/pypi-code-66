# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='deal',
    version='4.2.0',
    description='Programming by contract',
    python_requires='>=3.6',
    project_urls={"repository": "https://github.com/orsinium/deal"},
    author='Gram',
    author_email='master_fess@mail.ru',
    license='MIT',
    keywords='deal contracts pre post invariant decorators validation pythonic functional',
    classifiers=[
        'Development Status :: 5 - Production/Stable', 'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python', 'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance'
    ],
    entry_points={"flake8.extension": ["DEAL = deal.linter:Checker"]},
    packages=[
        'deal', 'deal._cli', 'deal._decorators', 'deal.linter',
        'deal.linter._extractors'
    ],
    package_dir={"": "."},
    package_data={
        "deal": ["*.typed"],
        "deal.linter": [
            "stubs/cpython/*.json", "stubs/cpython/http/*.json",
            "stubs/cpython/urllib/*.json", "stubs/dateutil/*.json",
            "stubs/dateutil/parser/*.json", "stubs/dateutil/tz/*.json",
            "stubs/dateutil/zoneinfo/*.json", "stubs/marshmallow/*.json",
            "stubs/pytz/*.json", "stubs/requests/*.json",
            "stubs/urllib3/*.json", "stubs/urllib3/contrib/*.json",
            "stubs/urllib3/util/*.json"
        ]
    },
    install_requires=[
        'astroid', 'hypothesis', 'pygments', 'typeguard', 'vaa>=0.2.1'
    ],
    extras_require={
        "dev": [
            "coverage", "isort[pyproject]", "m2r", "marshmallow", "mypy",
            "pytest", "pytest-cov", "recommonmark", "sphinx",
            "sphinx-rtd-theme", "urllib3"
        ],
        "docs": [
            "m2r", "recommonmark", "sphinx", "sphinx-rtd-theme", "urllib3"
        ],
        "tests": [
            "coverage", "isort[pyproject]", "marshmallow", "mypy", "pytest",
            "pytest-cov", "urllib3"
        ]
    },
)
