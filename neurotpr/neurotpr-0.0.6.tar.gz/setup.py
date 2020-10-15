import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neurotpr", 
    version="0.0.6",
    author="Jimin Wang and Yingjie Hu",
    author_email="yhu42@buffalo.edu",
    description="A Neuro-net ToPonym Recognition model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geoai-lab/NeuroTPR",
    packages=setuptools.find_packages(),
    install_requires=[
          'keras==2.3.1',
          'tensorflow==1.14.0 ',
          'tensorflow-hub==0.9.0',
          'emoji==0.6.0',
          'nltk==3.5'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)