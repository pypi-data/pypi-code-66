from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='fpgatools',
    version='0.0.1',
    author='József Fintor',
    author_email='fintor976@gmail.com',
    description='University project to support FPGA development.',
    long_description=open('README.md').read(),
    url='https://github.com/Fint0r/FPGA_Tools',
    license='MIT',
    classifiers=classifiers,
    keywords=['fpga', 'development', 'xdc', 'testbench'],
    packages=find_packages(),
    install_requires=['PyQt5']
)
