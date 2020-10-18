from setuptools import setup

setup(
    name='gomoku',
    description='Gomoku AI',
    author='Allen Zhang',
    version='v0.1.0',
    packages=[
        'gomoku',
        'gomoku.player',
        'gomoku.threat',
    ],
    install_requires=[
        'pytest',
        'gmpy2',
    ],
)
