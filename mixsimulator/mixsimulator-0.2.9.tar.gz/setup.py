import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mixsimulator",
    version="0.2.9",
    author="RASOANAIVO Andry, ANDRIAMALALA Rahamefy Solofohanitra, ANDRIAMIZAKASON Toky Axel",
    author_email="tokyandriaxel@gmail.com",
    description="Python application with nevergrad optimization model for calculating and simulating the least cost of an energy Mix under constraints.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Foloso/MixSimulator",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

