
from django.conf.urls import include, url
from . import actions

urlpatterns = [
    url(r'^list$',                    actions.List.as_view(),     name='gene_list'),
    url(r'^create$',                  actions.Create.as_view(),   name='gene_create'),
]