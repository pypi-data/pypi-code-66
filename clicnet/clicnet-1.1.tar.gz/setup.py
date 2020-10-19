import setuptools

INSTALL_DEPS = [
    "numpy>=1.17.3",
    "pandas>=1.0.3",
    "lifelines>=0.24.9",
    "seaborn>=0.11.0",
    "matplotlib>=3.3.1",
    "numexpr>=2.7.1"
]

with open("README.md", "r") as fh:
    long_description = "".join(fh.readlines()[1:])

setuptools.setup(
    name="clicnet",
    version="1.1",
    author="Ayal B. Gussow, Noam Auslander",
    author_email="ayal.gussow@gmail.com, noamaus@gmail.com",
    description="Clinical Clustering of Cancer patients based on neural NETworks (CLICnet).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://clicnet.pythonanywhere.com",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=INSTALL_DEPS
)
