# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from setuptools import setup, find_packages
import os
import shutil

_major = '0.0'
_minor = '0.0'

shutil.copy('../.license', 'LICENSE.txt')

if os.path.exists('../major.version'):
    with open('../major.version', 'rt') as bf:
        _major = str(bf.read()).strip()

if os.path.exists('../minor.version'):
    with open('../minor.version', 'rt') as bf:
        _minor = str(bf.read()).strip()

VERSION = '{}.{}'.format(_major, _minor)
SELFVERSION = VERSION
if os.path.exists('patch.version'):
    with open('patch.version', 'rt') as bf:
        _patch = str(bf.read()).strip()
        SELFVERSION = '{}.{}'.format(VERSION, _patch)

NAME = "azure-ml-component"

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: Other/Proprietary License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS',
    'Operating System :: POSIX :: Linux'
]

DEPENDENCIES = [
    'azureml-core',
    'azureml-telemetry',
    'psutil'
]

version_data = "VERSION = '%s'\n" % VERSION
with open('azure/ml/component/dsl/_version.py', 'w') as fout:
    fout.write(version_data)

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()
with open('../.inlinelicense', 'r', encoding='utf-8') as f:
    inline_license = f.read()

setup(
    name=NAME,
    version=SELFVERSION,

    description='',
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type='text/x-rst',
    author='Microsoft Corp',
    license=inline_license,
    url='https://docs.microsoft.com/en-us/azure/machine-learning/service/',

    classifiers=CLASSIFIERS,

    packages=find_packages(exclude=["*.tests", "tests", "samples"]),
    include_package_data=True,

    install_requires=DEPENDENCIES,
    entry_points={
        'azureml_cli_subgroup_providers': [
            'component = azure.ml.component._cli.component_subgroup:ComponentSubGroup'
        ]
    },
    extras_require={
        'notebooks': [
            'ipywidgets',
            'packaging',
            'azure-storage-blob',
            'nbconvert<6',
            'papermill<2',
            'nteract-scrapbook'
        ]
    },
)
