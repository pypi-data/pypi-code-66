from setuptools import setup

with open('./README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='exabyte_json_include',
    version='2020.10.19',
    description='An extension for json_include to support file inclusion',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/Exabyte-io/json_include',
    author='Exabyte Inc.',
    author_email='info@exabyte.io',
    py_modules=['json_include'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development'
    ]
)
