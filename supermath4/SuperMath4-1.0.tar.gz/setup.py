# coding=utf-8

from distutils.core import setup

setup(
    name='SuperMath4',    # 对外我们模块的名字
    version='1.0',       # 版本号
    description='这是第一个对外发布的模块，测试哦',  # 描述
    author='LittleBai',   # 作者
    author_email='930017955@qq.com',
    py_modules=['SuperMath4.demo1', 'SuperMath4.demo2']
)

# import setuptools
#
# with open("README.md", "r") as fh:
#     long_description = fh.read()
#
# setuptools.setup(
#     name="SuperMath4",
#     version="0.0.1",
#     author="Example Author",
#     author_email="930017955@qq.com",
#     description="A small example package",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/pypa/sampleproject",
#     packages=setuptools.find_packages(),
#     classifiers=[
#         'SuperMath4.demo1', 'SuperMath4.demo2'
#     ],
# )