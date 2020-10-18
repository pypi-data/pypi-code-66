from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="git-sign-off",
    version="0.0.0",
    description="Sign off git certificates for tasks and check them.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Alberto Ferreira",
    author_email="AlbertoEAF@users.noreply.github.com",
    url="https://github.com/AlbertoEAF/git-sign-off",
    packages=find_packages(exclude=["tests"]),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "git-sign-off = git_sign_off.__main__:main_sign",
            "git-sign-off-check = git_sign_off.__main__:main_check",
        ]
    },
)
