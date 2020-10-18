from setuptools import setup


setup(
    name='pyearl',
    version='0.0.1',
    author='limyel',
    author_email='limyel@qq.com',
    url='https://github.com/lim-mil/pyearl',
    description='一个简单的 Python 框架',
    packages = ['pyearl'],
    install_requires=['werkzeug'],
    entry_points={
        'console_scripts': [

        ]
    }
)
