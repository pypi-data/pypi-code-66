from setuptools import setup, find_packages

setup(name="Vins__server_messenger",
      version="0.2",
      description="Vins__server_messenger",
      author="Gregory Vins",
      author_email="gregoryvins@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
