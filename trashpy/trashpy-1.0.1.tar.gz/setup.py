import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trashpy",
    version="1.0.1",
    author="Paul Bailey",
    author_email="paul.m.bailey@gmail.com",
    description="Download your Google Drive Trash folder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pizzapanther/pydrive-trash-backup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['google-api-python-client', 'google-auth-oauthlib'],
    entry_points={
        'console_scripts': [
            'trashpy = trashpy.main:main',
        ],
    }
)
