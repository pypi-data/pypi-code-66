import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="worldpops",
    version="2",
    author="GadhaGod",
    author_email="gadhaguy13@gmail.com",
    description="Get live population, population rank, yearly change, and density of any country.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gadhagod/worldpops",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	install_requires=['requests']
)
