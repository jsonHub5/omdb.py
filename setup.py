#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        return fp.read()


def parse_requirements(filename):
    return [line.strip()
            for line in read(filename).strip().split('\n')
            if line.strip()]

pkg = {}
exec(read('src/omdb/__pkg__.py'), pkg)

readme = read('README.rst')
changelog = read('CHANGELOG.rst')
requirements = parse_requirements('requirements.txt')


setup(
    name=pkg['__package_name__'],
    version=pkg['__version__'],
    url=pkg['__url__'],
    license=pkg['__license__'],
    author=pkg['__author__'],
    author_email=pkg['__email__'],
    description=pkg['__description__'],
    long_description=readme + '\n\n' + changelog,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
    keywords='omdb imdb movies',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
