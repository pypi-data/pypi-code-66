from setuptools import setup 

# reading long description from file 
with open('DESCRIPTION.rst') as file: 
	long_description = file.read() 


# specify requirements of your package here 
REQUIREMENTS = ['googletrans'] 

# some more details 
CLASSIFIERS = [ 
	'Development Status :: 4 - Beta', 
	'Intended Audience :: Developers', 
	'Topic :: Internet', 
	'License :: OSI Approved :: MIT License', 
	'Programming Language :: Python', 
	'Programming Language :: Python :: 2', 
	'Programming Language :: Python :: 2.6', 
	'Programming Language :: Python :: 2.7', 
	'Programming Language :: Python :: 3', 
	'Programming Language :: Python :: 3.3', 
	'Programming Language :: Python :: 3.4', 
	'Programming Language :: Python :: 3.5'
	] 

# calling the setup function 
setup(name='tweetprep', 
	version='1.0.1', 
	description='A small preprocessor for tweets.', 
	long_description=long_description,
	url='https://github.com/garain/tweetprep', 
	author='Avishek Garain', 
	author_email='avishekgarain@gmail.com', 
	license='MIT', 
	packages=['prep'],
	classifiers=CLASSIFIERS, 
	install_requires=REQUIREMENTS, 
	keywords='tweet translate preprocess'
	) 
