
from django.conf.urls import include, url
from . import handlers

urlpatterns = [
    url(r'^create$', handlers.Create.as_view(),   name='sequences_create'),
]