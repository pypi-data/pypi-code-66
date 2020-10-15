import os
import sys
from setuptools import find_packages, setup

version = '0.0.3'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if 'upload' in sys.argv:
    print("You should make a tag now as well.")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")

setup(
    name='rrpproxy',
    version=version,
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    description='A python connector for RRP Proxy',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Tech',
    author_email='tech@byte.nl',
    url='https://github.com/ByteInternet/rrpproxy',
    download_url='https://github.com/ByteInternet/rrpproxy/archive/20201012.1.tar.gz',
    python_requires='>=3.4',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
