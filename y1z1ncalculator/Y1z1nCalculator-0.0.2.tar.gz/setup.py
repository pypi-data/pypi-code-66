from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Y1z1nCalculator',
  version='0.0.2',
  description='Simple calc',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Yazan Talib',
  author_email='y1z1n.xx@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Y1z1nSimple', 
  packages=find_packages(),
  install_requires=['json'] 
)
