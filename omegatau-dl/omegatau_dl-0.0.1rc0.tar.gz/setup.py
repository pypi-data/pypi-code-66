import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "omegatau_dl",
    version = "0.0.1rc0",
    author = "Marcel Johannfunke",
    author_email = "jakunddexter@gmail.com",
    description = ("Skript to download all episodes from omegataupodcast.net"),
    license = "GPL3",
    keywords = "omegatau omegataupodcast",
    url = "https://gitlab.com/mjohannfunke/omegatau-download",
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    install_required = [
        'requests',
    ]
)
