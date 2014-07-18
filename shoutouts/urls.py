from django.conf.urls import patterns, include, url
from .views import shoutout_list, shoutout_detail, ShoutOutDetail, ShoutOutList, ShoutOutCreate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moza_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',ShoutOutList.as_view(), name='shoutout_list'),
    url(r'^create/$', ShoutOutCreate.as_view(), name='shoutout-create'),
    url(r'^(?P<pk>\d+)/$', ShoutOutDetail.as_view(), name='shoutout-detail'),
)
