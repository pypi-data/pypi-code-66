from setuptools import setup, find_namespace_packages
from pathlib import Path

def load_if_exist(file_name, req=False):
    f = Path(file_name)
    if f.exists():
        with open(f) as fd:
            if req:
                return  fd.read().splitlines()
            else:
                return fd.read()
    return ''

PKG_NAME = 'adcc_backup'


setup(
    name=PKG_NAME,
    author='Marco Treglia',
    author_email='marco.treglia@akka.eu',
    url='https://gitlabee.dt.renault.com/ADCC/server_backup/-/tree/develop',
    version='0.6.2',
    license=load_if_exist('LICENSE'),
    description='Upload data',
    long_description=load_if_exist('README.md'),
    packages=find_namespace_packages(include=[PKG_NAME, f'{PKG_NAME}.*']),
    entry_points={'console_scripts': [f'{PKG_NAME}_server = {PKG_NAME}.scripts:adcc_backup_server_main',
                                      f'{PKG_NAME}_client = {PKG_NAME}.scripts:adcc_backup_client_main',
                                      f'{PKG_NAME}_utils = {PKG_NAME}.scripts:adcc_backup_utils_main']},
    install_requires=load_if_exist('requirements.txt',req=True),
    include_package_data=True,
    package_data={
      PKG_NAME : ['requirements.txt', 'README.md', 'LICENSE'],
    },
    python_requires='>=3.7'
)
