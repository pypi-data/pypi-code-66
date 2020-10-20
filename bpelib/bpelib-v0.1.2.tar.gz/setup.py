from distutils.core import setup, Extension
import os
from pathlib import Path


version = "0.1.0"

with open("README.rst", "r") as file:
    long_description = file.read()


def setup_with_c_libs():
    boost_c = [str(path) for path in Path("bpe/libc/boost").rglob("*.c")]
    boost_cpp = [str(path) for path in Path("bpe/libc/boost").rglob("*.cpp")]
    boost_h = [str(path) for path in Path("bpe/libc/boost").rglob("*.h")]
    boost_hpp = [str(path) for path in Path("bpe/libc/boost").rglob("*.hpp")]
    rel_boost_c = [path.replace(str(Path("bpe/libc")) + os.path.sep, '')
                   for path in boost_c]
    rel_boost_cpp = [path.replace(str(Path("bpe/libc")) + os.path.sep, '')
                     for path in boost_cpp]
    rel_boost_h = [path.replace(str(Path("bpe/libc")) + os.path.sep, '')
                   for path in boost_h]
    rel_boost_hpp = [path.replace(str(Path("bpe/libc")) + os.path.sep, '')
                     for path in boost_hpp]

    setup(name="bpelib",
          version=version,
          description="Byte Pair Encoding for Natural Language Processing.",
          long_description=long_description,
          author="skyzip",
          author_email="skyzip96@gmail.com",
          url="https://gitlab.com/Skyzip/bpelib",
          ext_modules=[
              Extension(
                  "bpelib.bpe.libc.bpelibc",
                  sources=[
                              "bpe/libc/_bpelibc.cpp",
                              "bpe/libc/string_utils.cpp",
                              "bpe/libc/word_freq_utils.cpp"
                          ] + boost_c + boost_cpp,
                  include_dirs=[
                      "bpe/libc/boost/include"
                  ]
              )
          ],
          packages=[
              "bpelib",
              "bpelib.bpe",
              "bpelib.bpe.libc"
          ],
          package_dir={
              "bpelib": ".",
              "bpelib.bpe": "bpe",
              "bpelib.bpe.libc": "bpe/libc"
          },
          package_data={
              "bpelib": ["__init__.py", "README.rst"],
              "bpelib.bpe": ["__init__.py", "bpe.py"],
              "bpelib.bpe.libc": [
                                     "_bpelibc.cpp",
                                     "string_utils.cpp",
                                     "word_freq_utils.cpp",
                                     "string_utils.hpp",
                                     "word_freq_utils.hpp"
                                 ] + rel_boost_c + rel_boost_cpp + rel_boost_h + rel_boost_hpp
          },
          install_requires=[
              "numpy",
              "tqdm"
          ],
          license="MIT",
          classifiers=[
              "Programming Language :: Python :: 3",
              "Operating System :: OS Independent",
          ]
          )


def setup_without_c_libs():
    setup(name="bpelib",
          version=version,
          description="Byte Pair Encoding for Natural Language Processing.",
          long_description=long_description,
          author="skyzip",
          author_email="skyzip96@gmail.com",
          url="https://gitlab.com/Skyzip/bpelib",
          packages=[
              "bpelib",
              "bpelib.bpe",
          ],
          package_dir={
              "bpelib": ".",
              "bpelib.bpe": "bpe",
          },
          package_data={
              "bpelib": ["__init__.py", "README.rst"],
              "bpelib.bpe": ["__init__.py", "bpe.py"],
          },
          install_requires=[
              "numpy",
              "tqdm"
          ],
          license="MIT",
          classifiers=[
              "Programming Language :: Python :: 3",
              "Operating System :: OS Independent",
          ]
          )


def main():
    print("setting up bpelib version: " + version)

    try:
        setup_with_c_libs()
    except (Exception, SystemExit) as exception:
        print(exception)
        print("Trying to build without C libraries ...")
        setup_without_c_libs()


if __name__ == '__main__':
    try:
        if os.environ.get('CI_COMMIT_TAG'):
            print("Getting CI_COMMIT_TAG.")
            version = os.environ['CI_COMMIT_TAG']
        else:
            version = os.environ['CI_JOB_ID']
            print("Getting CI_JOB_ID.")
    except KeyError:
        print("Unable to get environment variable.")
        print("Setting version manually to: " + str(version))

    main()
