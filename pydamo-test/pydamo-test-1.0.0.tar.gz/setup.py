import setuptools

with open("README.md", "r", encoding = 'utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydamo-test",
    version="1.0.0",
    author="bode135",
    author_email='2248270222@qq.com', # 作者邮箱
    description="pydamo with dm.dll and auto-regsvr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bode135/pydamo', # 主页链接
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    # include_package_data=True,
    # package_data={"": ['dm.dll']},
    data_files = [( '', ['pydamo_0\\dm.dll'] )],

    # packages=[str('nanomsg'), str('_nanomsg_ctypes'), str('nanomsg_wrappers')],
    # data_files=[('lib\\site-packages\\',["C:\\Dev\\external\\nanomsg\\x86\\Release\\nanomsg.dll"])],

    python_requires='>=3.6',
    install_requires=['pywin32', 'bode-time'], # 依赖模块
)
