"""
Jupyter notebook site generator

Author:  Anshul Kharbanda
Created: 10 - 18 - 2020
"""
from setuptools import setup

# Read README.md
with open('README.md', 'r') as f:
    readme = f.read()

# Setup function
setup(
    name='callystio',
    version='0.0.0',
    description='Jupyter notebook site generator',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/andydevs/callystio',
    author='Anshul Kharbanda',
    author_email='akanshul97@gmail.com',
    license='MIT',
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    packages=["callystio"],
    include_package_data=True
)