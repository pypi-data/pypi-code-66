from setuptools import setup, find_packages

setup(name="messenger_client_project",
      version="0.0.2",
      description="messenger_client_project",
      author="Andrei Karachenko",
      author_email="andrey141294@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
