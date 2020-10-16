import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybitlaunch", 
    version="1.1.0",
    author="BitLaunch",
    author_email="support@bitlaunch.io",
    description="pybitlaunch is a python client library for accessing the BitLaunch API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bitlaunchio/pybitlaunch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)