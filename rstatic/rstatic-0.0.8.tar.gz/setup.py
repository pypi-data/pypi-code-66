#!/usr/bin/env python

"""rStatic (Rebatch Static Site Generator).

Copyright (c) 2020 Joshua Powell. All rights reserved.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import find_packages
from setuptools import setup

"""PyPi Information

    Additional PyPi information and how to configure the setup definition
    can be found at https://pypi.org/classifiers/
"""

setup(
    name='rstatic',
    version='0.0.8',
    author='Joshua Powell',
    description='Open-source static site generator.',
    url='https://rebatch.io/rstatic',
    packages=find_packages(),
    include_package_data=True,
    zip_safe = False,
    install_requires=[
        'flask',
        'frozen-flask',
        'flask-flatpages',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Framework :: Flask",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
)