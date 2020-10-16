import setuptools

with open("README.md", "r") as readmeFile:
    README = readmeFile.read()

setuptools.setup(
    name="download_images",
    version="1.0",
    author="Akhilesh Chandorkar",
    author_email="akhilesh.chandorkar@gmail.com",
    description="Package that downloads images from google",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Xarcrax/download_images",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["selenium"],
    keywords='images, download, google',
    project_urls={
        'Bug Reports': 'https://github.com/Xarcrax/download_images/issues',
        'Buy me a coffee': 'https://ko-fi.com/xarcrax',
        'Say Thanks!': 'https://saythanks.io/to/akhilesh.chandorkar%40gmail.com',
        'Source': 'https://github.com/Xarcrax/download_images/sampleproject/',
    }
)
