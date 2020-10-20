from pathlib import Path
from setuptools import setup
import os

here = Path(os.path.dirname(os.path.abspath(__file__)))
root = here.parent

version_ns = {}
with open(root / 'voila' / '_version.py') as f:
    exec(f.read(), {}, version_ns)
version = version_ns['__version__']


def get_data_files():
    """Get the data files for the package.
    """
    data_files = []
    # Add all the templates
    subdir = 'share/jupyter/voila/templates/'
    for (dirpath, dirnames, filenames) in os.walk(subdir):
        print(dirpath)
        print("***", filenames)
        if filenames:
            filenames = [f for f in filenames if f.endswith('.map')]
            data_files.append((str(dirpath), [os.path.join(dirpath, filename) for filename in filenames]))
    for k in data_files:
        print("...", k)
    return data_files


setup(
    name="voila-sourcemaps",
    version=version,
    description='Source maps for Voila',
    data_files=get_data_files(),
    include_package_data=True,
    install_requires=[f'voila=={version}'],
    url='https://github.com/voila-dashboards/voila',
    author='Voilà Development team',
    author_email='jupyter@googlegroups.com',
    zip_safe=False,
)