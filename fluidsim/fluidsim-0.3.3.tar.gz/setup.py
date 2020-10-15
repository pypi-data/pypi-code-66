import os
import sys
from pathlib import Path

from time import time
from runpy import run_path

from setuptools import setup, find_packages

from transonic.dist import make_backend_files, init_transonic_extensions

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

here = Path(__file__).parent.absolute()

sys.path.insert(0, ".")

from setup_configure import FFTW3, logger, TRANSONIC_BACKEND
from setup_build import FluidSimBuildExt

time_start = time()


build_dependencies_backends = {
    "pythran": ["pythran>=0.9.7"],
    "cython": ["cython"],
    "python": [],
    "numba": [],
}

if TRANSONIC_BACKEND not in build_dependencies_backends:
    raise ValueError(
        f"FLUIDSIM_TRANSONIC_BACKEND={TRANSONIC_BACKEND} "
        f"not in {list(build_dependencies_backends.keys())}"
    )

setup_requires = []
setup_requires.extend(build_dependencies_backends[TRANSONIC_BACKEND])

# Set the environment variable FLUIDSIM_SETUP_REQUIRES=0 if we need to skip
# setup_requires for any reason.
if os.environ.get("FLUIDSIM_SETUP_REQUIRES", "1") == "0":
    setup_requires = []


def long_description():
    """Get the long description from the relevant file."""
    with open(os.path.join(here, "README.rst")) as readme:
        lines = list(readme)

    idx = lines.index(".. description\n") + 1
    return "".join(lines[idx:])


# Get the version from the relevant file
version = run_path("fluidsim/_version.py")
__version__ = version["__version__"]
__about__ = version["__about__"]

# Get the development status from the version string
if "a" in __version__:
    devstatus = "Development Status :: 3 - Alpha"
elif "b" in __version__:
    devstatus = "Development Status :: 4 - Beta"
else:
    devstatus = "Development Status :: 5 - Production/Stable"

install_requires = [
    "fluiddyn >= 0.3.2",
    "h5py",
    "h5netcdf",
    "transonic>=0.4.3",
    "setuptools_scm",
    "xarray",
]

if FFTW3:
    from textwrap import dedent
    from warnings import warn

    fft_extras_msg = dedent(
        """
        *********************************************************************

        FFTW was detected, but pyfftw and fluidfft will not be auto-installed
        (which was the case in previous fluidsim versions). To do so, instead
        of:

            pip install fluidsim

        specify "extras":

            pip install "fluidsim[fft]"

        *********************************************************************
    """
    )
    warn(fft_extras_msg)

console_scripts = [
    "fluidsim = fluidsim.util.console.__main__:run",
    "fluidsim-test = fluidsim.util.testing:run",
    "fluidsim-create-xml-description = fluidsim.base.output:run",
]

for command in ["profile", "bench", "bench-analysis"]:
    console_scripts.append(
        "fluidsim-"
        + command
        + " = fluidsim.util.console.__main__:run_"
        + command.replace("-", "_")
    )


def transonize():

    paths = [
        "fluidsim/base/time_stepping/pseudo_spect.py",
        "fluidsim/base/output/increments.py",
        "fluidsim/operators/operators2d.py",
        "fluidsim/operators/operators3d.py",
        "fluidsim/solvers/ns2d/solver.py",
        "fluidsim/solvers/ns3d/strat/solver.py",
        "fluidsim/solvers/ns3d/forcing.py",
    ]
    make_backend_files([here / path for path in paths], backend=TRANSONIC_BACKEND)


def create_pythran_extensions():
    import numpy as np

    compile_arch = os.getenv("CARCH", "native")
    extensions = init_transonic_extensions(
        "fluidsim",
        backend=TRANSONIC_BACKEND,
        include_dirs=np.get_include(),
        compile_args=("-O3", f"-march={compile_arch}", "-DUSE_XSIMD"),
    )
    return extensions


def create_extensions():
    if "egg_info" in sys.argv:
        return []

    logger.info("Running fluidsim setup.py on platform " + sys.platform)
    logger.info(__about__)

    transonize()

    ext_modules = create_pythran_extensions()

    logger.info(
        "The following extensions could be built if necessary:\n"
        + "".join([ext.name + "\n" for ext in ext_modules])
    )

    return ext_modules


setup(
    version=__version__,
    long_description=long_description(),
    author="Pierre Augier",
    author_email="pierre.augier@legi.cnrs.fr",
    url="https://foss.heptapod.net/fluiddyn/fluidsim",
    license="CeCILL",
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        devstatus,
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        # actually CeCILL License (GPL compatible license for French laws)
        #
        # Specify the Python versions you support here. In particular,
        # ensure that you indicate whether you support Python 2,
        # Python 3 or both.
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["doc", "examples"]),
    setup_requires=setup_requires,
    install_requires=install_requires,
    cmdclass={"build_ext": FluidSimBuildExt},
    ext_modules=create_extensions(),
    entry_points={"console_scripts": console_scripts},
)

logger.info(f"Setup completed in {time() - time_start:.3f} seconds.")
