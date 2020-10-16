import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='fotoparadies-orders-cli-avra',
      version='0.1a1',
      description='Unofficial command line interface for keeping track of dm Fotoparadies orders.',
      scripts=['./scripts/fotoparadies'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/StefanAvra/fotoparadies-orders-cli',
      author='Stefan Avramescu',
      author_email='stefan.avra@gmail.com',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      packages=setuptools.find_packages(),
      python_requires='>=3.6',
      )