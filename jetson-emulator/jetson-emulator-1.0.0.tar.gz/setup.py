import setuptools

def readme():
    with open('README.rst') as f:
        return f.read()
		
setuptools.setup(

	name = "jetson-emulator",
	version = "1.0.0",
	author = "Tea Vui Huang",
	author_email = "tvhuang@hotmail.com",
	description = "Emulator of NVIDIA Jetson AI-computer for makers, learners, developers and students",
	keywords = 'deep-learning GPU jetson emulator AI edge-computing computer vision inference image classification object detection segmentation',
	long_description = readme(),
	long_description_content_type = "text/markdown",
	url = "https://github.com/teavuihuang/jetson-emulator",
	packages=setuptools.find_packages(),
    classifiers = ['Development Status :: 5 - Production/Stable','Intended Audience :: Developers','Intended Audience :: Education','Intended Audience :: Science/Research','License :: OSI Approved :: MIT License','Operating System :: Microsoft :: Windows','Operating System :: POSIX :: Linux','Programming Language :: Python','Programming Language :: Python :: 3','Topic :: Scientific/Engineering :: Artificial Intelligence','Topic :: Software Development','Topic :: System :: Hardware','Topic :: Scientific/Engineering :: Image Recognition','Topic :: System :: Emulators','Environment :: GPU :: NVIDIA CUDA'],
	license='MIT',
	python_requires = '>=3.7.9',
	install_requires=[
        'matplotlib>=3.2.2',
        'numpy>=1.18.5'
	]	

)

