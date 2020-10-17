from setuptools import setup, find_packages, Extension
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3' 
]

setup(
    name = 'nidhichaudharygsmtpd007',
    version = '1.0.6',
    description='A library to convert the google sheets into pandas df and plot the graphs accordingly',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Nidhi Chaudhary',
    author_email='nidhichaudhary1097@gmail.com',
    License='MIT',
    classifiers=classifiers,
    keywords='GoogleSheets, Plotting',
    packages=find_packages(),
    install_requires=[]
)