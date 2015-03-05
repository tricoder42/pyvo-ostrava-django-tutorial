from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'dlog.views.home', name='home'),
    url(r'^blog/', include('dlog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
