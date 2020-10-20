from setuptools import find_packages, setup

setup(
    name='ctfdumper',
    version="1.0.1",
    description="Dumps all of the submissions from a CTFD site to a csv file.",
    author="ghostccamm",
    keywords="ctfd dumper submission",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=[
        "pandas",
        "requests",
        "tqdm",
        "urllib3"
    ],
    entry_points={
        "console_scripts" : [
            "ctfdumper = ctfdumper.run:main"
        ]
    },
    python_requires='>=3.6'
)
