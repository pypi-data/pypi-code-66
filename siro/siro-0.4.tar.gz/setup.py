from distutils.core import setup
setup(
  name = 'siro',
  packages = ['siro'],
  version = '0.4',
  license='MIT',
  description = 'This is a package for controlling the SIRO SmartHome Devices like rollers.',
  author = 'Felix Arnold',
  author_email = 'moin@felix-arnold.dev',
  url = 'https://github.com/fear/siro',
  download_url = 'https://github.com/fear/siro/archive/0.4.tar.gz',
  keywords = ['SmartHome', 'Siro', 'roller', 'home assistant'],
  install_requires=[
          'asyncio',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Utilities',
    'Topic :: Home Automation',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
