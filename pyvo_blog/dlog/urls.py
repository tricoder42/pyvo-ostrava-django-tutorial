from django.conf.urls import url
from dlog.views import detail, entry_create


urlpatterns = [
    url(r'^create/', entry_create, name='entry_create'),
    url(r'^detail/(?P<slug>[^/]+)', detail, name='entry_detail')
]