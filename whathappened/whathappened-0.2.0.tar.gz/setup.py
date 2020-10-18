import setuptools

import versioneer

# check to prevent dirty uploads to PyPI
if versioneer.get_versions()["dirty"]:

    class MustCommitError(Exception):
        pass

    raise MustCommitError("please commit everything before releasing")

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []

test_requirements = ['pytest', 'pytest-cov', 'pytest-watch', 'pytest-reportlog']

setuptools.setup(
    author="Rollcloud",
    author_email="roullcloud@gmail.com",
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    cmdclass=versioneer.get_cmdclass(),
    description="A changelog generator using simply structured git commit messages.",
    entry_points={'console_scripts': ['whathappened=whathappened.command_line:main']},
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="whathappened",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    test_suite='tests',
    tests_require=test_requirements,
    url="https://github.com/Rollcloud/whathappened",
    version=versioneer.get_version(),
)
