#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='profanity',
    description='Simple profanity filter.',
    author='Christian Oudard',
    author_email='christian.oudard@gmail.com',
    url='https://github.com/christian-oudard/profanity',
    license='BSD',
    version='0.1.0',
    packages=find_packages('.'),
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=True,
    include_package_data=True,
    test_suite='nose.collector',
)
