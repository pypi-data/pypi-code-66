import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="noip_api-CodeGuy3", # Replace with your own username
    version="0.0.1",
    author="CodeGuy3",
    author_email="kiko.smire@gmail.com",
    description="A small noip api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeGuy3/noip_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)