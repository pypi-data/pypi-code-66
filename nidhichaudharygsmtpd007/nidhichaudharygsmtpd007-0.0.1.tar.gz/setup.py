from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3' 
]

setup(
    name = 'nidhichaudharygsmtpd007',
    version = '0.0.1',
    description='A library to convert the google sheets into pandas df and plot the graphs accordingly',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Nidhi Chaudhary',
    author_email='nidhichaudhary1097@gmail.com',
    License='MIT',
    classifiers=classifiers,
    keywords='GoogleSheets, Plotting',
    packages=find_packages(),
    install_requires=['Pandas', 'gspread', 'oauth2client', 'Matplotlib']
)