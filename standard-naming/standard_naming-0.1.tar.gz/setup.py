from setuptools import setup, find_packages
 
classifiers = [
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'Programming Language :: Python :: 3',
  'License :: OSI Approved :: MIT License',
]
 
setup(
  name='standard_naming',
  version='0.1',
  description='Achieving semantic consistency of name-identity',
  long_description=open('README.txt').read(),
  url='',  
  author='Blair Huang',
  author_email='Blair1217@outlook.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Natural Language Processing', 
  packages=find_packages(),
  install_requires=[] 
)