import setuptools
import io

def parse_requirements(filename):
    lineiter=(line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Python-EasyGraph",                                     
    version="0.2a9",                                        
    author="Fudan MSN Group",                                       
    author_email="easygraph@163.com",                      
    description="Easy Graph",                            
    long_description=long_description,                      
    long_description_content_type="text/x-rst",          
    url="https://github.com/easy-graph/Easy-Graph",                              
    packages=setuptools.find_packages(),                    
    classifiers=[                                           
        "Programming Language :: Python :: 3",              
        "License :: OSI Approved :: BSD License",           
        "Operating System :: OS Independent",               
    ],
    install_requires=parse_requirements("requirements.txt"),
)

