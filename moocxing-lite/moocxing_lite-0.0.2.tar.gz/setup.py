from setuptools import setup, find_packages

setup(
    name = 'moocxing_lite',
    version = '0.0.2',
    keywords='moocxing',
    description = 'anzhi',
    license = 'MIT License',
    url = '',
    author = 'anzhi',
    author_email = '1532741445@qq.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [
        'requests>=2.24.0',
        'pyserial>=3.4',
        'PyAudio>=0.2.11',
        'mcpi>=1.2.0',
        'minecraftstuff>=1.0.1',
        'baidu-aip>=2.2.18.0',
        'bs4>=0.0.1',
        'ffmpeg-python>=0.2.0',
        'paho-mqtt>=1.5.0',
        'xpinyin>=0.5.6',
        ],
   
)
