from django.conf.urls import url
from dlog.views import detail, entry_create, entry_update, entry_delete


urlpatterns = [
    url(r'^create/', entry_create, name='entry_create'),
    url(r'^detail/(?P<slug>[^/]+)', detail, name='entry_detail'),
    url(r'^update/(?P<slug>[^/]+)', entry_update, name='entry_update'),
    url(r'^delete/(?P<slug>[^/]+)', entry_delete, name='entry_delete'),
]