import setuptools

setuptools.setup(
    name="grpc-powergate-client",
    version="0.9.0",
    author="Textile",
    author_email="contact@textile.io",
    url="https://github.com/textileio/powergate",
    packages=setuptools.find_packages(),
    install_requires=[
      'protobuf',
    ],
)
