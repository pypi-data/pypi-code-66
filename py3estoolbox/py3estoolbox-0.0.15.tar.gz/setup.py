from distutils.core import setup
setup(
  name          = 'py3estoolbox',
  packages      = ['py3estoolbox'],
  version       = '0.0.15',
  description   = 'A Python3 Elasticsearch tools and utilities collection',
  author        = 'Great Tomorrow',
  author_email  = 'gr82morozr@gmail.com',
  url           = 'https://gr82morozr@bitbucket.org/gr82morozr/py3-estoolbox.git',  
  download_url  = 'https://gr82morozr@bitbucket.org/gr82morozr/py3-estoolbox.git', 
  keywords      = ['Utility', 'Tools', 'Elasticsearch' ], 
  classifiers   = [],
  install_requires=[ 'elasticsearch', 'elasticsearch_dsl', 'py3toolbox']
)
