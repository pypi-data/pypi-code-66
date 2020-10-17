from distutils.core import setup
setup(
  name = 'protlego',         # How you named your package folder (MyLib)
  packages = ['protlego'],   # Chose the same as "name"
  version = '1.0.4',      # Start with a small number and increase it with every change you make
  description = 'A python package for the automated construction of chimeras and analysis',   # Give a short description about your library
  author = 'Noelia Ferruz',                   # Type in your name
  author_email = 'noelia.feruz@domain.com',      # Type in your E-Mail
  url = 'https://github.com/Hoecker-Lab/protlego',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Hoecker-Lab/protlego/archive/1.0.0.tar.gz',    # I explain this later on
  keywords = ['PROTEIN DESIGN', 'CHIMERAGENESIS', 'PROTEIN EVOLUTION', 'NETWORK THEORY', 'FUZZLE'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
            'numpy=>1.18.1',
            'scipy',
            'csb',
            'moleculekit',
            'matplotlib',
            'graph-tool',
            'openmm',
            'mdtraj',
            'pandas',
	    'boost=1.69.0',
	    'boost-cpp=1.69.0',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
