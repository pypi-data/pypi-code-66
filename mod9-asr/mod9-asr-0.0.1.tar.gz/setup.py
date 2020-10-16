#!/usr/bin/env python3

import setuptools

with open('README.md') as f_in:
    long_description = f_in.read()

with open('requirements.txt') as f_in:
    requirements = [requirement for requirement in f_in]

setuptools.setup(
    name='mod9-asr',
    version='0.0.1',
    description='Wrappers over Mod9 ASR Engine TCP Server.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mod9 Technologies',
    author_email='support@mod9.com',
    license='BSD 2-Clause',
    url='http://mod9.io/python-sdk',
    # TODO: classifiers?
    # TODO: platforms?
    packages=setuptools.PEP420PackageFinder.find(),
    # TODO: namespace_packages?
    install_requires=requirements,
    # TODO: extras_require?
    # TODO: python_requires?
    # TODO: scripts?
    # TODO: include_package_data?
    # TODO: zip_safe?

    # Installs executable under user's PATH.
    entry_points={
        'console_scripts': ['mod9-rest-server = mod9.rest.server:main'],
    },
)
