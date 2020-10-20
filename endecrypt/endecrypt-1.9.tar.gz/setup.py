
from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

import endecrypt

setup(
    name='endecrypt', 
    version="1.9",
    author="Rajyavardhan Bithale",
    author_email="bithale03@protonmail.com",
    description="A simple python library for encryption and decryption . Library contain 10 (version 1.0) including ciphers and various other cryptography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajyavardhanb/endecrypt",
    py_modules=['endecrypt'],
    scripts=['endecrypt.py'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
