import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metathethaurus_client-timoderbeste", # Replace with your own username
    version="0.0.1",
    author="Timo Wang",
    author_email="ntwang1994@gmail.com",
    description="A small client for interacting with metathethaurs apis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)