from setuptools import setup, find_packages

install_requires = [
    'numpy',
    'matplotlib'
]


setup(
    name="numerical_analysis",
    version="0.0.1",
    packages=find_packages(),

    author="IAGerogiannis",
    author_email='iagerogiannis@gmail.com',
    description="Basic numerical analysis tools, useful for parameterization of aerodynamic shapes, like airfoils, "
                "or ducts.",
    url="https://github.com/iagerogiannis/numerical-analysis",
    install_requires=install_requires,
    license="BSD"
)
