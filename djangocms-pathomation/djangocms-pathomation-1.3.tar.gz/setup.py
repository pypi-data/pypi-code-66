from setuptools import setup, find_packages

setup(
    name='djangocms-pathomation',
    version='1.3',
    author='Pathomation',
    author_email='info@pathomation.com',
    packages=find_packages(),
    install_requires=[
        'wheel',
        'requests',
        'requests-toolbelt',
        'pandas',
        'pma-python'
    ]
)



