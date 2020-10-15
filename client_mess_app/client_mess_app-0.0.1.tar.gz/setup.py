from setuptools import setup, find_packages

setup(name="client_mess_app",
      version="0.0.1",
      description="client_messenger_app",
      author="Aleksandr Kositsyn",
      author_email="kos_off@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
