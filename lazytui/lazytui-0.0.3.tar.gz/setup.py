from pathlib import Path
from setuptools import setup

from lazytui import version as VERSION

# The directory containing this file
cur_dir = Path(__file__).parent

# The text of the README file
README = (cur_dir / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='lazytui',
    version=VERSION,
    description='A terminal UI for the la(z)yperson',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/kylepollina/lazytui',
    author='Kyle Pollina',
    author_email='kylepollina@pm.me',
    license='MIT',
    # classifiers=[
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.7',
    # ],
    packages=['lazytui'],
    include_package_data=True,
    # entry_points={
    #     'console_scripts': [
    #         'embedmd=embedmd.core:embedmd'
    #     ]
    # },
)
