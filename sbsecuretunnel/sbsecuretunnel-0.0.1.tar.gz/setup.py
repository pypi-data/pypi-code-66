import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sbsecuretunnel",
    version="0.0.1",
    author="CrossBrowserTesting",
    author_email="info@crossbrowsertesting.com",
    description="A wrapper for Smartbear SecureTunnel, to make testing local sites easier in CrossBrowserTesting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crossbrowsertesting/sb_securetunnel_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.2',
    install_requires=["requests"]
)