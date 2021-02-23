#!/usr/bin/env python

# Purpose = Package and distribution management.

from setuptools import setup, find_packagees

with open("README.md", "r") as fh:
    readme_long_description = fh.read()

with open('LICENSE') as fh:
    license_long_description = fh.read()

setup(
    name = 'extractGEO',
    packages = ['extractGEO'],
    version = '0.1.0',
    url = 'https://github.com/cetienn01/extractGEO',
    description = 'Python dataset retriever',
    long_description = readme_long_description,
    long_description_content_type = 'text/markdown',
    author = 'Chris Etienne', 'Arman Aksoy',
    author_email = 'cetienn01@gmail.com', 'arman@aksoy.org',
    keywords=['python', 'GEO'],
    license = license_long_description,
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License'
    ],
    # packages=find_packages(exclude=('tests', 'docs'))
    packages=['extractGEO'],
    include_package_data = True,
    install_requires = ['numpy, 'pandas'],
    scripts = ['scripts/<name-of-script.py>'],
    entry_points={'console_scripts': ['extractGEO=reader.__main__:main']},

)
