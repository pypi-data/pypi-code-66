import setuptools


setuptools.setup(
    name="phypi",
    version="0.0.1",
    author="Manas Mishra",
    author_email="mk1316a@gmail.com",
    description="A physics python libary",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manas1316am/phypi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[

    ],
    extras_require={
        "dev": [
            "pytest >= 3.7",
        ]
    },
)
