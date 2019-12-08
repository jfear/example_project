#!/usr/bin/env python

from setuptools import setup

requirements = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name="example_project",
    version="0.0.1",
    description="Local library for the example project",
    author="Justin M Fear",
    author_email="justin.m.fear@gmail.com",
    url="https://github.com/jfear/example_project",
    packages=["example_project"],
    install_requires=requirements,
    license="MIT license",
)
