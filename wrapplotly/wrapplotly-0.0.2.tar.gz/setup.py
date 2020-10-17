import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wrapplotly",
    version="0.0.2",
    author="Jillian Augustine",
    author_email="jaugur.ds@gmail.com",
    description="A plotly wrapper allowing subplots and single plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jill-augustine/wrapplotly",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)