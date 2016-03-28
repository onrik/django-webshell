from django.conf.urls import patterns, url
from .views import execute_script_view

urlpatterns = patterns('',
    url(r'^execute/$', execute_script_view, name='execute-script'),
)
