from setuptools import setup

setup(
    name='sp_yt_search',
    packages={
        'sp_yt_search',
        'sp_yt_search.SpSearch',
        'sp_yt_search.YtSearch',
    },
    version='1.0.2',
    license='MIT',
    description='Parse Spotify URI to youtube link',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    author='Marcin Myśliwiec',
    author_email='marcin.mysliw@gmail.com',
    url='https://github.com/MarcinMysliwiec/sp_yt_searcher',
    download_url='https://github.com/MarcinMysliwiec/sp_yt_searcher/blob/master/dist/sp_yt_search-1.0.2.tar.gz',
    keywords=['sp_yt_search', 'yt', 'sp'],
    install_requires=['requests==2.24.0', 'spotipy==2.16.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
