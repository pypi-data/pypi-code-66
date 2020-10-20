import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zcmd",
    version="0.0.6",
    author="ouczbs",
    author_email="ouczbs@qq.com",
    description="A package use for jupyter notebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ouczbs/zcmd",
    packages=setuptools.find_packages(),
    license='MIT',
)
