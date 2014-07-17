from django.conf.urls import patterns, include, url
from .views import shoutout_list, shoutout_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moza_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',shoutout_list, name='shoutout_list'),
    url(r'^(?P<pk>\d+)/$', shoutout_detail, name='shoutout-detail'),
)
