#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="sentry-dingding-feelys",
    version='0.2.1',
    author='lcfevr',
    author_email='lcfevr@163.com',
    url='https://github.com/lcfevr/sentry-dingding-feelys',
    description='ding talk sentry plugin',
    license='MIT',
    keywords='sentry dingtalk',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_dingding_feelys = sentry_dingding_feelys.plugin:DingTalkPlugin'
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
