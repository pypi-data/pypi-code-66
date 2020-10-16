from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3',
    'Operating System :: Microsoft :: Windows :: Windows 10'
]

setup(
    name="win10note",
    version="0.0",
    packages=find_packages(),
    long_description=open('README.rst').read(),
    author="Xyndra",
    author_email="sammy@deutschergamingserver.de",
    license="MIT",
    keywords=["note", "notification", "win10", "Windows 10"],
    description="A time calculator",
    classifiers=classifiers,
    install_requires=['win10toast']
)
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# py setup.py sdist
