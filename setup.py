#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

import guitest

setup(
    name='guitest',
    version="0.1",
    license='GPLv3',
    author="0.1",
    author_email='github@konchris.de',

    description='Test creating standalone executables with GUI in Python 3.5',

    packages=find_packages(),

    url='https://github.com/konchris/guitest/',

)
