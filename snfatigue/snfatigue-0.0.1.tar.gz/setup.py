from setuptools import setup, find_packages
import os

this_dir = os.path.dirname(__file__)

with open(os.path.join(this_dir, "readme.md"), "rb") as fo:
    long_description = fo.read().decode("utf8")

setup(
    name='snfatigue',
    package_dir={"": "src"},
    py_modules=['snfatigue'],
    description='SN fatigue calculations',
    install_requires=[l.strip() for l in open('requirements.txt').readlines()],
    extras_require={"dev": ["pytest ~= 4.6"]},
    python_requires=">=3.6, <4",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rafael Rossi',
    url='https://github.com/haphaeu/snfatigue',
    license="GPL2",
)