from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="rlapis",
    packages=find_packages(),
    include_package_data=True,
    version="0.0.1",
    description="API for multi/single external RL Gym environments",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Raphael Van Hoffelen",
    author_email="dskart11@gmail.com",
    license="MIT",
    install_requires=["numpy", "fastapi", "uvicorn", "gym"],
    url="https://github.com/dskart/rlapis",
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
)
