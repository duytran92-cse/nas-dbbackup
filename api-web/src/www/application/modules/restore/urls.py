
from django.conf.urls import include, url
from . import handlers

urlpatterns = [
    url(r'^list$',    handlers.List.as_view(),      name='exon_list'),
    url(r'^create$', handlers.Create.as_view(),   name='exon_create'),
]
