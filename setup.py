from distutils.core import setup
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
    packages=['webshell'],
    package_data={'webshell': [
        'templates/webshell/*.html',
        'migrations/*.py',
        'static/css/*.css',
        'static/js/*.js'
    ]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
