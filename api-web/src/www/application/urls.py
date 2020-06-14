from django.conf.urls import include, url

urlpatterns = [
    url(r'^bucket/',                  include('application.modules.bucket.urls')),
    url(r'^backup/',                  include('application.modules.backup.urls')),
    url(r'^restore/',                 include('application.modules.restore.urls')),
]
