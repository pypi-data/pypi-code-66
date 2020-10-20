import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zcmd",
    version="0.0.5",
    author="ouczbs",
    author_email="ouczbs@qq.com",
    description="A package use for jupyter notebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ouczbs/zcmd",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[],
    python_requires='>=3.6',
)
