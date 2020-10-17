import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyorm", # Replace with your own username
    version="0.0.1",
    author="Domtryr",
    author_email="doffoufaye@gmail.com",
    description="The simple basic orm to permet has execute CRUD query method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Domtry/mini_orm.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)