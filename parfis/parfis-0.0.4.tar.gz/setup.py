import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parfis",
    version="0.0.4",
    author="Ginko Balboa",
    author_email="ginkobalboa3@gmail.com",
    description="Particles and field simulator",
    packages=setuptools.find_packages(include=['parfis', 'parfis.*']),
    package_data={"parfis": ['data/config/api_1.ini']},
    include_package_data=True,
    platforms=["Windows 10 x64"],
    extras_require={'plotting': ['matplotlib'],
                    'data': ['numpy'],
                    'testing':['unittest']},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GinkoBalboa/parfis",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: C++",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires='>=3.7',
    zip_safe=False,
)