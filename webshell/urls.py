from django.conf.urls import url
from .views import execute_script_view

urlpatterns = [
    url(r'^execute/$', execute_script_view, name='execute-script'),
]
