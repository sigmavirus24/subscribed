#!/usr/bin/env python

import sys
import os
from re import compile

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[1] in ('submit', 'publish'):
    os.system('python setup.py sdist upload')
    sys.exit()

sysv = sys.version[:3]

packages = ['subscribed']
requires = ['github3.py>=0.3', 'flask>=0.9']
del sysv

__version__ = ''
with open('gh/__init__.py') as fd:
    reg = compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        match = reg.match(line)
        if match:
            __version__ = match.group(1)
            break

if not __version__:
    raise RuntimeError('Cannot find version information')


setup(
    name='subscribed',
    version=__version__,
    author='Ian Cordasco',
    author_email='graffatcolmingov@gmail.com',
    url='https://github.com/sigmavirus24/subscribed',
    packages=packages,
    include_package_data=False,
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ]
    )
