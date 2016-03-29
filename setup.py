#-----------------------------------------------------------------------------
# Copyright (c) 2015, 'rkl' developers (see AUTHORS file)
# All rights reserved.
#
# Distributed under the terms of the MIT license.
#
# The full license is in the LICENSE file, distributed with this software.
#-----------------------------------------------------------------------------

from setuptools import setup, find_packages
# to use a consistent encoding
from codecs import open
from os import path

import versioneer

# custom setup.py commands
cmdclass = versioneer.get_cmdclass()

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rkl',
    version=versioneer.get_version(),
    description='Computational kernels common in radar signal processing',
    long_description=long_description,

    url='http://github.com/ryanvolz/rkl',

    author='Ryan Volz',
    author_email='ryan.volz@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],

    keywords='radar signal processing',

    packages=find_packages(),
    setup_requires=[],
    install_requires=['numba', 'numpy'],
    extras_require={
        'develop': ['flake8', 'nose', 'pylint', 'twine', 'wheel'],
        'doc': ['numpydoc', 'sphinx'],
    },
    cmdclass=cmdclass,
)
