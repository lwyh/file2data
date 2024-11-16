#!/usr/bin/python
# encoding:utf-8

from setuptools import setup, find_packages
 
setup(
    name="file2data",
    version="0.1",
    license="MIT Licence",
 
    url="https://github.com/lwyh/file2data",
    author="lwyh",
    author_email="lwyhnice@gmail.com",
 
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)