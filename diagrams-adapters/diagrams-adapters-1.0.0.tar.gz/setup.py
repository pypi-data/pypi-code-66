from setuptools import setup, find_packages


setup(
    author='Vladas Tamošaitis',
    author_email='amd.vladas@gmail.com',
    name='diagrams-adapters',
    description=(
        'Set of adapters to generate architecture diagrams '
        'from popular text file formats.'
    ),
    version="1.0.0",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        "typing-extensions; python_version < '3.8.0'",
        "diagrams",
    ],
)
