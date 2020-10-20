from setuptools import setup, find_namespace_packages

PKG_NAME = 'adcc_backup'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name=PKG_NAME,
    author='Marco Treglia',
    url='https://gitlabee.dt.renault.com/ADCC/server_backup/-/tree/develop',
    version='0.6.0',
    license=license,
    description='Upload data',
    long_description=readme,
    packages=find_namespace_packages(include=[PKG_NAME, f'{PKG_NAME}.*']),
    entry_points={'console_scripts': [f'{PKG_NAME}_server = {PKG_NAME}.scripts:adcc_backup_server_main',
                                      f'{PKG_NAME}_client = {PKG_NAME}.scripts:adcc_backup_client_main',
                                      f'{PKG_NAME}_utils = {PKG_NAME}.scripts:adcc_backup_utils_main']},
    install_requires=requirements,
    include_package_data=True,
    python_requires='>=3.7'
)
