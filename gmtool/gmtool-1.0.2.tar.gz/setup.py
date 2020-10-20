from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='gmtool',
      version='1.0.2',
      description='A powerful generation tool',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Gmwang',
      author_email='550146647@qq.com',
      url='https://www.python.org/',
      license='MIT',
      keywords='generation',
      project_urls={
            'Documentation': 'https://www.apple.com.cn/',
            'Funding': 'https://www.apple.com.cn/',
            'Source': 'https://www.apple.com.cn/',
            'Tracker': 'https://www.apple.com.cn/',
      },
      packages=setuptools.find_packages(),
      install_requires=['numpy>=1.14'],
      python_requires='>=3'
     )