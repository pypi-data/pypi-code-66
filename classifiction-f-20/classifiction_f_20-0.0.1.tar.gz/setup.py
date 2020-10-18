import setuptools
with open("README.md","r")as fh:
    long_description =fh.read()
setuptools.setup(    
    name = "classifiction_f_20",
    version = "0.0.1",
    author = "karen",
    author_email = "962388544@qq.com",
    description = "Used to predict the properties of f_20",
    long_description =long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages = setuptools.find_packages(),
    package_data={
		'':['*.pkl']
	},
    classifiers=[
    "Programming Language :: Python :: 2",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires='>=2.6',     
)