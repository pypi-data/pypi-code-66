import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anymate",
    version="0.0.4",
    author="Anymate ApS",
    author_email="simon@anymate.io",
    description="Anymate SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anymate/AnymatePythonSDK",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)