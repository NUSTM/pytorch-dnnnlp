#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dnnnlp
from setuptools import setup, find_packages

with open("readme.md", "r", encoding='utf-8') as fobj:
    long_description = fobj.read()

setup(
    name="dnnnlp",
    version="1.0.3",
    author="KzXuan",
    author_email="kaizhouxuan@gmail.com",
    description="Deep Neural Networks for Natural Language Processing classification or sequential task written by PyTorch.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/NUSTM/pytorch-dnnnlp",
    packages=find_packages(),
    install_requires=[
        "torch >= 1.2.0",
        ],
    classifiers=[
        "License :: Free for non-commercial use",
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
