from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="raptor-framework",
    version="0.0.1",
    author="Igor Dantas de Aguiar",
    author_email="igordantas91@icloud.com",
    description="Raptor Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/IgorDantasID/",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)