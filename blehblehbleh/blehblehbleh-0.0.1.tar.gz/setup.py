from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3' 
]

setup(
    name = 'blehblehbleh',
    version = '0.0.1',
    description='An app to convert the google sheets into pandas df',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Nidhi Chaudhary',
    author_email='nidhichaudhary1097@gmail.com',
    License='MIT',
    classifiers=classifiers,
    keywords='google sheets in python',
    packages=find_packages(),
    install_requires=['Pandas', 'gspread', 'oauth2client']
)