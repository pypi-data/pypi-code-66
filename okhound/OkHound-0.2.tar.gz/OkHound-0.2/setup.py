##############################################################################
# Copyright 2017 SoundHound, Incorporated.  All rights reserved.
##############################################################################
import os
import sys
from setuptools import setup, Extension

if sys.platform.startswith('win'):
    # not supported
    print('windows platform not supported')
    exit(0)
elif sys.platform.startswith('darwin'):
    # osx
    module1 = Extension("okhound",
                        sources=["pyOkHound.cpp"],
                        libraries=["PhraseSpotter"],
                        library_dirs=["libdir_osx"])
elif sys.platform.startswith('linux'):
    if os.uname()[4].startsWith("arm"):
        # python
        module1 = Extension("okhound",
                            sources=["pyOkHound.cpp"],
                            libraries=["PhraseSpotter"],
                            library_dirs=["libdir_pi"])
    else:
        # linux
        module1 = Extension("okhound",
                            sources=["pyOkHound.cpp"],
                            libraries=["PhraseSpotter"],
                            library_dirs=["libdir_linux"])
else:
    # unknown
    print('unknown platform - could not install')
    exit(0)

setup(name='OkHound',
      version='0.2',
      description="'Ok Hound' phrase spotter",
      ext_modules=[module1],
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      author='Soundhound Inc.',
      maintainer='Oliver Yeun',
      url='https://github.com/oyeun/okhound',
      download_url='https://github.com/oyeun/okhound/archive/0.1.tar.gz',
      keywords=['OkHound']
      )
