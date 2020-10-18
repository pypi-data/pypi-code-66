from setuptools import setup
import re

with open('indexPy\__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

print("Setup for version: ", version)

requirements = ["requests"]

with open("README.md", "r") as f:
    readme = f.read()

setup(name="indexPy",
      packages=["indexPy"],
      author='Angel Carias',
      author_email=None,
      version=version,
      description="Python3 wrapper for PyPi API",
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires=">=3.6",
      url="https://github.com/angelCarias/indexPy",
      download_url="https://github.com/angelCarias/indexPy/archive/v0.1.0.tar.gz"
      )