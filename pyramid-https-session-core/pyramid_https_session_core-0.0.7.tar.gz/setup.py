"""pyramid_https_session_core installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

# store version in the init.py
import re

with open(
    os.path.join(os.path.dirname(__file__), "pyramid_https_session_core", "__init__.py")
) as v_file:
    VERSION = re.compile(r'.*__VERSION__ = "(.*?)"', re.S).match(v_file.read()).group(1)

# Pyramid Requirements:
# 1.4 add_request_method
# 1.5 SignedCookieSessionFactory, for tests
install_requires = [
    "pyramid>=1.5",
]
tests_require = [
    "pytest",
]
testing_extras = tests_require + []

setup(
    name="pyramid_https_session_core",
    version=VERSION,
    description="provides for a 'session_https' secure session interface",
    long_description="This package is EOL and support has been discontinued.",
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="web pyramid beaker",
    packages=["pyramid_https_session_core"],
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    url="https://github.com/jvanasco/pyramid_https_session_core",
    license="MIT",
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "testing": testing_extras,
    },
    test_suite="tests",
)
