from setuptools import setup
import os
import io

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
BASE_DIR = os.path.join(os.path.dirname(__file__))

with io.open(os.path.join(BASE_DIR, "requirements.txt"), encoding="utf-8") as fh:
    REQUIREMENTS = fh.read()

setup(
    name="warker",
    version="1.1",
    description="Leave the tedious operation to the back end",
    author="Isclub Studio",
    url="https://github.com/isclub/warker",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    install_requires=REQUIREMENTS,
    long_description_content_type="text/markdown",
    license="MIT License",
)
