#!/usr/bin/env python
from setuptools import setup, find_packages                                                                                                                                           

import os
execfile(os.path.join("TGScheduler", "release.py"))

packages=find_packages()

if os.path.isdir('locales'):
    packages.append('locales')

setup(
    name="TGScheduler",
    version=version,
    description=description,
    long_description=long_description,
    author=author,
    author_email=email,
    url=url,
    license=license,
    platforms=["any"],
    install_requires=[
       'TurboGears2', 
    ],
    zip_safe=False,
    packages=packages,
    #package_data=package_data,
    keywords=[
        'turbogears.widgets', 'tg2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: TurboGears',
        'Framework :: TurboGears :: Widgets',
    ]
    )
