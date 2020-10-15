from setuptools import setup, find_packages

setup(name="messenger_server_project",
      version="0.0.2",
      description="messenger_server_project",
      author="Andrei Karachenko",
      author_email="iv.iv@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
