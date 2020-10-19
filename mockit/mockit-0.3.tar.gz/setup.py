from distutils.core import setup


setup(
    name="mockit",
    packages=["mockit"],
    version="0.3",
    license="MIT",
    description="Easy REST API mocking tool.",
    author="Victor Vasiliev",
    author_email="victorvasil93@gmail.com",
    url="https://github.com/victorvasil93/mockit",
    keywords=["MOCK", "SERVER", "REST", "API", "TESTS"],
    install_requires=["Flask", "pytest"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
)
