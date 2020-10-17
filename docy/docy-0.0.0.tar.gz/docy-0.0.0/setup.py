import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="docy",
    version="0.0.0",
    author="Sepehr Kalanaki",
    author_email="prowidgs@gmail.com",
    description="Mark-Down to HTML documentation generator written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OverShifted/Docy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
