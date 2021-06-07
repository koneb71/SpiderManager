#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

from SpiderManager import __version__, __author__

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name='SpiderManager',
    version=__version__,
    description='Admin ui for spider service',
    long_description=
    'Go to https://github.com/koneb71/SpiderManager/ for more information.',
    author=__author__,
    author_email='koneb71@gmail.com',
    url='https://github.com/koneb71/SpiderManager/',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,

    entry_points={
        'console_scripts': {
            'spidermanager = SpiderManager.run:main'
        },
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
)
