import setuptools


def load_content(path):
    '''
    加载文件内容。
    '''

    with open(path, 'r', encoding='utf-8') as reader:
        return reader.read()


setuptools.setup(
    name='suoran',
    version='0.0.3',
    description='extends sanic',
    long_description=load_content('readme.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/chenshenchao/suoran',
    keywords='sanic suoran',
    license='MIT',
    author='chenshenchao',
    author_email='chenshenchao@outlook.com',
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=setuptools.find_packages(
        exclude=['test']
    ),
    install_requires=[
        'sanic>=20.9.0',
        'tortoise-orm>=0.16.16',
        'aiomysql>=0.0.20',
    ]
)
