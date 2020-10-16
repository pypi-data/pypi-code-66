from setuptools import setup
from os.path import join, dirname

setup(name='pulling',
      version='1.2',
      packages=['pulling'],
      license='Apache License 2.0',
      author='ItYaS',
      author_email='ryaboshapkoseraph@gmail.com',
      url='https://github.com/ItYaS/pulling',
      python_requires='>=3.5.1',
      description='Repository for parsing data from files and sites.',
      long_description=open(join(dirname(__file__), 'README.txt')).read(),
      zip_safe=False)
