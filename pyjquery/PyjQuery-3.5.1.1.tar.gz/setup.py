# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='PyjQuery',  # Required

    version='3.5.1.1',  # Required

    description='The Write Less, Do More, JavaScript Library for DicksonUI',  # Optional

    long_description=long_description,  # Optional

    # text/plain, text/x-rst, and text/markdown
    long_description_content_type='text/markdown',  # Optional (see note above)

    url='https://github.com/Ksengine/DicksonUI/extentions/jquery',  # Optional

    author='Kavindu Santhusa',  # Optional

    author_email='kavindusanthusa@gmail.com',  # Optional

    classifiers=[  # Optional
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS 9',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: MS-DOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 3.1 or Earlier',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: Microsoft :: Windows :: Windows 95/98/2000',
        'Operating System :: Microsoft :: Windows :: Windows CE',
        'Operating System :: Microsoft :: Windows :: Windows NT/2000',
        'Operating System :: Microsoft :: Windows :: Windows Server 2003',
        'Operating System :: Microsoft :: Windows :: Windows Server 2008',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: Microsoft :: Windows :: Windows XP',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: AIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: BSD/OS',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: BSD :: NetBSD',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: POSIX :: GNU Hurd',
        'Operating System :: POSIX :: HP-UX',
        'Operating System :: POSIX :: IRIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Other',
        'Operating System :: POSIX :: SCO',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Operating System :: Unix',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless'
    ],

    keywords='fast, small, feature-rich, JavaScript, library\
,HTML, document, traversal, manipulation, event handling,\
 animation, Ajax, simpler, easy, versatility, extensibility, cross-browser',  # Optional

    #   Alternative for single source projects
    py_modules=["jquery"],
    scripts=["jquery.py"],
    #

    install_requires=['DicksonUI'],  # Optional

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/Ksengine/DicksonUI/issues',
        'Source': 'https://github.com/Ksengine/DicksonUI/extentions/jquery',
    },
)
