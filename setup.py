#!/usr/bin/env python
from setuptools import setup, find_packages

PACKAGE = 'ecmc'
NAME = 'pyecmc'
KEYWORDS = ('aws', 'elasticache', 'memcached')
VERSION = '0.1.1'
DESCRIPTION = 'A Python module that wraps python-memcached with AWS Elasticache autodiscovery.'
LICENSE = 'LGPL'
URL = 'https://github.com/saebyn/pyecmc'
AUTHOR = 'John Weaver'
AUTHOR_EMAIL = 'saebynx+pyecmc@gmail.com'

setup(
    name=NAME,
    version=VERSION,
    keywords=KEYWORDS,
    description=DESCRIPTION,
    license=LICENSE,

    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,

    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['python-memcached', 'hash_ring'],
)
