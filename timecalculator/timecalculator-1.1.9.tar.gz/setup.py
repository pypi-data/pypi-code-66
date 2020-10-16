from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'Operating System :: Microsoft :: Windows :: Windows 10'
]

setup(
    name="timecalculator",
    version="1.1.9",
    packages=find_packages(),
    long_description=open('README.rst').read(),
    author="Xyndra",
    author_email="sammy@deutschergamingserver.de",
    license="MIT",
    url='https://github.com/Xyndra/Timecalculator',
    keywords=["time","calculator"],
    description="A time calculator",
    classifiers=classifiers
)
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# py setup.py sdist