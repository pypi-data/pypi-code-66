from setuptools import setup, find_packages

setup(name="Vins_client_messenger",
      version="0.2",
      description="Vins_client_messenger",
      author="Gregory Vins",
      author_email="gregoryvins@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
