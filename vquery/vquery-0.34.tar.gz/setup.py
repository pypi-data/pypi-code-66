from setuptools import setup

setup(
	name = "vquery",
	version = "0.34",
	author = "Jakob Svanholm",
	author_email = "rymdlego@gmail.com",
	url = "https://github.com/rymdlego/vquery",
        download_url = "https://github.com/rymdlego/vquery/archive/v0.34.tar.gz",
	description = "A tool for querying vCenter for various information.",
	keywords = "vSphere VMware vCenter",
	scripts=['vq'],
	packages=['vquery'],
	install_requires=['docopt', 'pyVmomi', 'future', 'six']
)
