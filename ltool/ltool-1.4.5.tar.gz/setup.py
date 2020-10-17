#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 07:53:46 2020

@author: nick
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
ver = "1.4.5"
setuptools.setup(
    # Application name:
    name="ltool",

    # Version number (initial):
    version=ver,

    # Application author details:
    author="Nikos Siomos",
    author_email="nsiomos@noa.gr",

    # Packages
    packages=setuptools.find_packages(),
    
    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/ltool_v" + ver +"/",

    description="Automated aerosol layer detection algorithm.",
    
    long_description_content_type="text/markdown",

    # Dependent packages (distributions)
    install_requires=[
        "numpy",
        "datetime",
        "pandas",
        "xarray",
        "netCDF4"
    ],
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.7',
    entry_points={
          'console_scripts': ['ltool = ltool.__main__:main'],
      }
)
