from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^infounits/$', 'infounit_list', name='infounit_list'),
    url(r'^infounits/(?P<pk>[0-9]+)$', 'infounit_detail', name='infounit_detail'),
)
