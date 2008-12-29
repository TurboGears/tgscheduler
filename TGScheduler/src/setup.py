from setuptools import setup, find_packages                                                                                                                                           
from turbogears.finddata import find_package_data                                                                                                                                     

import os
execfile(os.path.join("tgcombine", "release.py"))

packages=find_packages()
package_data = find_package_data(where='tgcombine',
    package='tgcombine')

if os.path.isdir('locales'):
    packages.append('locales')
    package_data.update(find_package_data(where='locales',
        exclude=('*.po',), only_in_packages=False))

setup(
    name="TGScheduler",
    version=version,

    # uncomment the following lines if you fill them out in release.py
    description=description,
    author=author,
    author_email=email,
    url=url,
    #download_url=download_url,
    license=license,

    install_requires=[
        "TurboGears >= 1.0.1",
    ],
    zip_safe=False,
    packages=packages,
    package_data=package_data,
    keywords=[
        'turbogears.widgets',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: TurboGears',
        'Framework :: TurboGears :: Widgets',
    ],
    test_suite='nose.collector',
    )
