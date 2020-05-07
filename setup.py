#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'extractGEO',
    packages = ['extractGEO'],
    version = '0.1',
    url = 'https://github.com/cetienn01/extractGEO',
    description = 'Python dataset retriever',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Chris Etienne, Arman Aksoy',
    author_email = 'cetienn01@gmail.com, arman@aksoy.org',
    keywords=['python', 'GEO'],
    license = 'MIT',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License'
    ],
    install_requires=['numpy'],
    scripts = ['scripts/<name-of-script.py>']
)