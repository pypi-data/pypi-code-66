from setuptools import setup, find_packages

setup(name="OSolntseva_client",
      version="0.0.1",
      description="OSolntseva_client",
      author="Olga Solntseva",
      author_email="w-j-olga24@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
