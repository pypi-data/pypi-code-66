import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yh",
    version="0.0.2",
    author="icantsayrural",
    author_email="icantsayrural@disroot.org",
    description="yh!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/icantsayrural/yh",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        yh=yh.__main__:main
    ''',
)
