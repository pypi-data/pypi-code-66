from setuptools import setup, find_packages


setup(
    name='SingleCellFEM',
    version='0.1',
    packages=find_packages(),
    author='qingyun891',
    description='a single cell gene expression data analysis tool',
    long_description="...",
    url='https://github.com/qingyunpkdd/pylib',
    install_requires=["pyqt5==5.15.1","scipy==1.5.2","numpy==1.19.1","pandas==1.1.1","tqdm==4.49.0"],
    long_description_content_type="text/markdown",
    author_email='qingyun891@126.com')



