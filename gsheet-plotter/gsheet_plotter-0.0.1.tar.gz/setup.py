import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gsheet_plotter",
    version="0.0.1",
    author="Nitika Kamboj",
    author_email="nitika.kamboj92@gmail.com",
    description="A visualisation library written in Python to plot your Google Sheets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="google sheet api pandas dataframe matplotlib",
    url="https://github.com/Nitika-kamboj/gsheet_plotter",
    packages=['gsheet_plotter'],
    package_dir={'':'src'},
    install_requires=[
        "pandas",
        "matplotlib",
        "gsheet-api",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',)
