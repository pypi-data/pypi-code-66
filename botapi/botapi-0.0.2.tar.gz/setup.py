import pathlib

from setuptools import setup


def read(f):
    return (pathlib.Path(__file__).parent / f).read_text('utf-8').strip()


setup(
    name='botapi',
    version='0.0.2',
    packages=['botapi'],
    url='https://github.com/EdiBoba/botapi',
    license='Apache 2.0',
    author='Vyacheslav Rineisky',
    author_email='rineisky@gmail.com',
    description='Provides python api to sn and messengers',
    long_description=read('README.rst'),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
