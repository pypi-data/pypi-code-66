# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""
import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='mysql-operator',
    version='0.0.9',
    author='Jimmy Yeh',
    author_email='chienfeng0719@hotmail.com',
    description='A tool for backup/cleanup/migrate mysql',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chienfeng0719/mysql-operator',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'mysql-operator = mysql_operator:CliOperator.main'
        ]
    },
    python_requires='>=3.6',
)
