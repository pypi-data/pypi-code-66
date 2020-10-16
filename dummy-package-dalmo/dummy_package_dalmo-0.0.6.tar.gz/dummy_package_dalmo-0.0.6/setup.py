import setuptools
import os

setuptools.setup(
    name='dummy_package_dalmo',
    version='0.0.6',
    author='Marco Dal Molin',
    author_email='marco.dalmolin.1991@gmail.com',
    description='Test package to test CI with PyPI',
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.md")).read(),
    long_description_content_type='text/markdown',
    license='Apache Software License',
    classifiers=[
        'Development Status :: 3 - Alpha'  # https://martin-thoma.com/software-development-stages/
    ]
)
