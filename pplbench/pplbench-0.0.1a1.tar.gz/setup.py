# (c) Facebook, Inc. and its affiliates. Confidential and proprietary.

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pplbench",
    version="0.0.1a1",
    description="Evaluation framework for Probabilistic Programming Languages",
    author="Facebook, Inc.",
    license="MIT",
    keywords=[
        "Probabilistic Programming Language",
        "PPL",
        "Bayesian Inference",
        "Statistical Modeling",
        "MCMC",
        "Variational Inference",
        "PyTorch",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
