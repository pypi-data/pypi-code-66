#!/usr/bin/python

import setuptools

with open("README.md", "r") as input:
    ld = input.read()

setuptools.setup(
    name="easykvchat",
    version="1.0.0",
    author="ThisALV",
    author_email="lel.charriere@orange.fr",
    description="Ensemble client/serveur d'un système de messagerie.",
    long_description=ld,
    long_description_content_type="text/markdown",
    packages=["easykvchat", "easykvchat.client", "easykvchat.server"],
    install_requires=["kivy", "Twisted"],
    package_data={"": ["*.kv"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: French",
        "Topic :: Communications :: Chat"
    ],
    python_requires=">=3.8"
)
