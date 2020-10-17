# pystudy,LCid

# rm -rf bijou.egg-info build dist
# python setup.py sdist bdist_wheel bdist_egg
# python -m twine upload dist/*

# pip install bijou -i https://pypi.org/simple/


import setuptools
from distutils.core import setup
desc = '工具包的简要说明'

with open('README.md') as f:
    long_description = f.read()

# https://packaging.python.org/guides/distributing-packages-using-setuptools/
setup(
    name="testlibpy",                                   # 工具包名
    version="0.0.2",                                    # 版本
    author="pystudy",                               # 作者
    author_email="liuchen.chn@hotmail.com",               # 邮箱
    license='MIT',                                  # 软件许可协议
    description=desc,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://xxxxxx.com/xxxxxx/libPy",          # 项目链接
    classifiers=[                                   # https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',          # PyPI对项目进行分类的依据，以便于用户搜索
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords='',                                    # 关键词
    packages=setuptools.find_packages(include=['testlibpy']),  # 项目所包含的包
    py_modules=[],                                  # 包之外的独立模块文件名（不包含.py扩展名）
    install_requires=['numpy > 1.15'],
    python_requires='>=3.6',
)
