import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-your-bode135",
    version="0.0.1",
    author="bode135",
    author_email='2248270222@qq.com', # 作者邮箱
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bode135/pydamo', # 主页链接
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
