import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="procpipe",
    version="2020.10",
    author="Christian Daudt",
    author_email="csd@fixthebug.org",
    description="Simple data processing pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cdaudt/pipeline",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
