from django.conf.urls import patterns, url

urlpatterns = patterns('webshell.views',
    url(r'^execute/$', 'execute_script_view', name='execute-script'),
)