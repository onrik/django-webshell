Django-webshell
===============
Django application for running python code in your project's environment from django admin.

Installation
------------

    pip install git+https://github.com/onrik/django-webshell.git#egg=webshell

settings.py:

    INSTALLED_APPS = (
        ...
        'webshell',
        ...
    )

urls.py:

    urlpatterns = patterns('',
        ...
        (r'^webshell/', include('webshell.urls')),
        ...
    )
