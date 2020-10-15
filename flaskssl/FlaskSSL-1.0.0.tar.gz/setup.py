import os
import re
from setuptools import setup, find_packages


# Retrieve version number
def get_version(version_file=os.path.join(os.path.dirname(__file__),
                                          os.path.basename(os.path.dirname(__file__)),
                                          '_version.py')):
    """
    Retrieve the version of a python distribution.

    version_file default is the <project_root>/_version.py

    :param version_file: Path to version file
    :return: Version string
    """
    version_str_lines = open(version_file, "rt").read()
    version_str_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(version_str_regex, version_str_lines, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % version_file)


setup(
    install_requires=[
        'awsutils-s3>=0.2.1',
        'Flask>=1.0.2',
        'Flask-RESTful>=0.3.7',
        'synfo>=2.0.6',
    ],
    name='FlaskSSL',
    version=get_version('FlaskSSL/_version.py'),
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/sfneal/flask-ssl-validation',
    license='',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='SSL certification validation server.',
)