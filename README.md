Django-webshell
===============
Django application for running python code in your project's environment from django admin.

Installation
------------


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
