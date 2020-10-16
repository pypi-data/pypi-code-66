from distutils.core import setup
setup(
  name = 'SerinasDecisionTree',         
  packages = ['SerinasDecisionTree'],   
  version = '0.2',      
  license='MIT',       
  description = 'A Python package for decision-tree based classification of data',   
  author = 'Serina Grill',                  
  author_email = 'serinagrill@gmail.com',      
  url = 'https://github.com/serinamarie/SerinasDecisionTree',   
  download_url = 'https://github.com/serinamarie/SerinasDecisionTree/archive/v_02.tar.gz',   
  keywords = ['python', 'decision tree', 'classifier'],   
  install_requires=[         
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)


