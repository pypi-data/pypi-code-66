import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="litre-demo",
    version="0.0.1",
    author="Litre",
    author_email="litre-wu@tutanota.com",
    description="在线视频、音乐...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Litre-WU/demo",
    include_package_data=True,
    package_data={
        'templates': ['templates/*.html'],
        'static': ['static/*'],
        'docs': ['docs/*'],
        'logs': ['logs/*']
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
