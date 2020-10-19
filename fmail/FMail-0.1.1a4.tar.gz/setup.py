import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FMail",
    version="0.1.1a4",
    license='MIT',
    author="Atero645",
    author_email="",
    description="A small mail library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/Atero645/fmail/src/master/",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.6',
    extras_require={"dotenv": ["python-dotenv"]},
)
