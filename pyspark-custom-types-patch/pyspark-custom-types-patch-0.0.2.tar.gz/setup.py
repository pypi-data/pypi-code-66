import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyspark-custom-types-patch",
    version="0.0.2",
    author="KonstantinSk",
    author_email="borondondon@gmail.com",
    description="Package with workaround to handle new types in pyspark "
                "(for pyspark 3.0) ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["patches"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
