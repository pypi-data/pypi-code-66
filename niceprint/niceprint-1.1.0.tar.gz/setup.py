from setuptools import setup

setup(
    name="niceprint",
    version='1.1.0',
    author="AstralDev",
    author_email="ekureedem480@gmail.com",
    description="A simple module for print.",
    license="MIT",
    install_requires=["color"],
    data_files=[('',["./niceprint.py"])]
)
