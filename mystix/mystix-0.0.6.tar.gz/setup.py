import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mystix",
    version="0.0.6",
    author="Rowan Lindsay",
    author_email="development@rowanlindsay.com",
    description="A domain-specific language intended for "
                "event-driven acquisition, analysis, "
                "and visualization of data.",
    long_description=long_description.replace(":chart_with_downwards_trend:", ""),
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'numpy',
        'seaborn',
        'matplotlib',
        'pyqtgraph',
        'pyqt5',
        'mypy',
        'requests'
    ],
)