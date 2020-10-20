from setuptools import setup
import setuptools
setup(name='gmtool',
      version='1.0.1',
      description='A powerful generation tool',
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