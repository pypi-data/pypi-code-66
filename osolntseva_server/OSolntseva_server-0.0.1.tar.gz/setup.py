from setuptools import setup, find_packages

setup(name="OSolntseva_server",
      version="0.0.1",
      description="OSolntseva_server",
      author="Olga Solntseva",
      author_email="w-j-olga24@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
