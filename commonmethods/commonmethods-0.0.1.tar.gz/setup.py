from setuptools import setup

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name='commonmethods',
	version='0.0.1',
	description='This library contains some common methods that you don\'t wanna rewrite every time you make a new project.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	py_modules=['commonmethods'],
	package_dir={'':'src'},
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'Natural Language :: English'
	],
	install_requires=[],
	extras_requires={
		'dev': [
			'pytest>=3.7',
			'twine>=3.2',
			'check-manifest>=0.44'
		]
	}
)