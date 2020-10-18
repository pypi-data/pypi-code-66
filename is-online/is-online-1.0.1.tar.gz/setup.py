import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="is-online",
    version="1.0.1",
    author="Glenn Calleja Frendo",
    author_email="glenncal@gmail.com",
    description="A Python module meant for cli use which checks whether you are connected to the Internet.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glenncalleja/is_online",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["is_online=is_online.__main__:main"]},
    python_requires='>=3.6',
)
