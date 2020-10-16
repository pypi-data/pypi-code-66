from setuptools import setup, find_packages

setup(name="mess_client_eTcilopp",
      version="0.5.2",
      description="Messenger - client program",
      author="Alexander Kirikeza",
      author_email="kirikeza@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
