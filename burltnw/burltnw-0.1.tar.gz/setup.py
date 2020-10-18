from setuptools import setup, find_packages

def readme():
	with open('README.md') as f:
		return f.read()

setup(
	name='burltnw',
	version='0.1',
	description='module of lab robotics as use in develop application',
	long_description=readme(),
	url='https://github.com/tanawatthuamthet/burltnw',
	author='Tanawat',
	author_email='tempkakao@gmail.com',
	license='tnw',
	install_requires=[''],
	keywords=['burl','robot','apollo'],
	packages=['burltnw'],
	package_dir={'burltnw':'burltnw','Apollo_SDK_exe':'burltnw/Apollo_SDK_exe'},
	package_data={'burltnw':[
	'Apollo_SDK_exe/*.dll',
	'Apollo_SDK_exe/*.exe',
	'Apollo_SDK_exe/*.h'
	]},
	)