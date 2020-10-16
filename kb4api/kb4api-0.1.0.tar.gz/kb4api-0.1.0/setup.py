from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = ['kb4api']

requires = [
    'requests',
]

setup(
    name='kb4api',
    version='0.1.0',
    description='This is a Python wrapper for KnowBe4 API - https://developer.knowbe4.com/',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='midpipps',
    author_email='midpipps@gmail.com',
    url='https://github.com/midpipps/kb4api',
    install_requires=requires,
    license='LICENSE.md',
    packages=packages,
    keywords=['knowbe4', 'kb4api'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ],
)