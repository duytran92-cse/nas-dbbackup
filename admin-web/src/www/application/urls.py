from django.conf.urls import include, url
from . import actions

urlpatterns = [
    url(r'^backup/',                      include('application.modules.backup.urls')),
    #url(r'^bucket/',                      include('application.modules.bucket.urls')),
    url(r'^restore/',                      include('application.modules.restore.urls')),
    url(r'^$',                             actions.Home.as_view(), name='home'),
]
