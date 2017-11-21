#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

if __name__ == '__main__':
    package_name = 'adhoc_proto'

    description = 'Solution to the Ad Hoc "proto" problem.'

    with open('./COMMENTS.md', 'r') as file:
        long_description = file.read()

    install_requires = [
        # This package is needed by the application layer to implement
        # data models.
        'suitcase==0.10.2']

    setuptools.setup(name=package_name,
                     version='0.1.0',
                     description=description,
                     long_description=long_description,
                     license='MIT',
                     classifiers=['Programming Language :: Python :: 2.7'],
                     packages=setuptools.find_packages(exclude=['*.tests']),
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)
