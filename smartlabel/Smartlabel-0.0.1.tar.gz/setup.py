import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Smartlabel", # Replace with your own username
    version="0.0.1",
    author="Talha Abdullah",
    author_email="tahaabbu8@gmail.com",
    description="A command line interface to smartlabel.digital",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://smartlabel.digital/cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)