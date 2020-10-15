import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dictfilter',
    use_scm_version={
        'tag_regex': r'^(?P<prefix>v)?(?P<version>[^\+]+)$',
        'write_to': 'dictfilter/version.py'
    },
    author='Chris Latham',
    author_email='opensource@bink.com',
    description='Filter dictionaries based on a list of field names.',
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/binkhq/dictfilter',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
    setup_requires = [
        'setuptools-scm==4.1.2'
    ]
)
