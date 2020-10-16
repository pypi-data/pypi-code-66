from setuptools import setup, find_packages

setup(name="mess_server_eTcilopp",
      version="0.5.2",
      description="Messenger - server",
      author="Alexander Kirikeza",
      author_email="kirikeza@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
