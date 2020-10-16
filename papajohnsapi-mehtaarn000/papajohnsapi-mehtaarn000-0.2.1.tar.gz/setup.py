import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="papajohnsapi-mehtaarn000", # Replace with your own username
    version="0.2.1",
    author="mehtaarn000",
    author_email="arnavmehta1977@gmail.com",
    description="A python module that will allow users to use selenium to order pizza from Papa Johns.",
    long_description = long_description,
    url="https://github.com/mehtaarn000/papajohnsapi",
    packages=['papajohnsapi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)