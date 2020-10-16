import io
import os
from setuptools import setup


os.chdir(os.path.abspath(os.path.dirname(__file__)))


with io.open('README.rst', encoding='utf-8') as fp:
    description = fp.read()
setup(name='datamart-geo',
      version='0.2',
      packages=['datamart_geo'],
      install_requires=['requests', 'ngram-search'],
      description="Geographical location data",
      author="Remi Rampin",
      author_email='remi.rampin@nyu.edu',
      maintainer="Remi Rampin",
      maintainer_email='remi.rampin@nyu.edu',
      url='https://gitlab.com/ViDA-NYU/datamart/datamart-geo',
      project_urls={
          'Homepage': 'https://gitlab.com/ViDA-NYU/datamart/datamart-geo',
          'Source': 'https://gitlab.com/ViDA-NYU/datamart/datamart-geo',
          'Tracker': 'https://gitlab.com/ViDA-NYU/datamart/datamart-geo' +
                     '/-/issues',
      },
      long_description=description,
      license='BSD-3-Clause',
      keywords=['datamart'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'License :: Free for non-commercial use',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Database'])
