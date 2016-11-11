#!/usr/bin/env python

from setuptools import setup, find_packages
from webshell import __version__

DESCRIPTION = "Django application for running python code in your project's environment from django admin."

setup(
    name='django-webshell',
    version=__version__,
    description=DESCRIPTION,
    author='Andrey',
    author_email='and@rey.im',
    url='http://github.com/onrik/django-webshell',
    download_url='http://github.com/onrik/django-webshell/tarball/master',
    license='MIT',
    packages=find_packages(),
    package_data={'webshell': [
        'templates/webshell/*',
        'static/css/*',
        'static/js/*',
    ]},
    test_suite='runtests.runtests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
