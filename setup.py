#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plumbing",
    version="0.0.1",
    author="Failsafe",
    author_email="failsafe89@gmail.com",
    description="A pipeline programming architecture designed for mid-sized data processing, with an emphasis of simplicity over throughput/parallelisation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/failsafe89/plumbing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU LGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)