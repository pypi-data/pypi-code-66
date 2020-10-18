from setuptools import setup, find_packages

with open("README.md", mode="r") as file:
    l_desc = file.read()

setup(
    name="czech-covid19-data-api",
    version="1.0.5",
    author="Radek 'bednaJedna' Bednarik",
    packages=find_packages(),
    install_requires=["requests"],
    author_email="bednarik.radek@gmail.com",
    long_description=l_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/radekBednarik/czech-covid19-data-api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords="covid19 covid data czech Czechia public api wrapper python python3",
)