from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().split('\n')

setup_args = dict(
    name='scrapy_omdena_latam',
    version='0.0.1',
    description='Useful tools to work with Elastic stack in Python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Martin Hadid',
    author_email='martinhadid@gmail.com',
    keywords=['scrapy', 'scraper', 'omdena'],
    url='https://github.com/frapercan/scrapy_omdena_latam',
    download_url='https://pypi.org/project/scrapy_omdena_latam/'
)

if __name__ == '__main__':
    setup(**setup_args, install_requires=requirements)
