from setuptools import setup, Extension
from setuptools import find_packages

with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="colabjupyter",
        scripts=["scripts/colabcode"],
        version="0.0.9",
        description="ColabJupyter - Run Jupyter Lab On Colab",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Nekologist",
        author_email="ice@memeware.net",
        url="https://github.com/nekologist/colabjupyter",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        install_requires=["pyngrok>=4.1.12"],
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )
