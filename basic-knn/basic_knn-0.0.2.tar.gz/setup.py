import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="basic_knn",
    version="0.0.2",
    author="Ege Sabancı",
    author_email="egesabanci@outlook.com.tr",
    description="K-Nearest Neighbors algorithm for classification problems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Egesabanci/basic_knn",
    download_url = "https://pypi.org/project/basic_knn",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)