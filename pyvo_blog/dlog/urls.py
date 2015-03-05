from django.conf.urls import url
from dlog.views import detail


urlpatterns = [
    url(r'^detail/(?P<slug>[^/]+)', detail, name='entry_detail')
]