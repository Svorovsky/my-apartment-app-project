from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^infounits/$', 'infounit_list', name='infounit_list'),
    url(r'^infounits/(?P<pk>[0-9]+)$', 'infounit_detail', name='infounit_detail'),
    url(r'^deliveryservices/$', 'deliveryservice_list', name='task_list'),
    url(r'^deliveryservices/(?P<pk>[0-9]+)$', 'deliveryservice_detail', name='deliveryservice_detail'),
    url(r'^newsitems/$', 'newsitem_list', name='newsitem_list'),
    url(r'^newsitems/(?P<pk>[0-9]+)$', 'newsitem_detail', name='newsitem_detail'),
    url(r'^services/$', 'service_list', name='service_list'),
    url(r'^services/(?P<pk>[0-9]+)$', 'service_detail', name='service_detail'),
    url(r'^guests/$', 'guest_list', name='guest_list'),
    url(r'^guests/(?P<pk>[0-9]+)$', 'guest_detail', name='guest_detail'),
    url(r'^guestpasses/$', 'guestpass_list', name='guestpass_list'),
    url(r'^guestpasses/(?P<pk>[0-9]+)$', 'guestpass_detail', name='guestpass_detail'),
    url(r'^personalbills/$', 'personalbill_list', name='personalbill_list'),
    url(r'^personalbills/(?P<pk>[0-9]+)$', 'personalbill_detail', name='personalbill_detail'),
    url(r'^persons/$', 'person_list', name='person_list'),
    url(r'^persons/(?P<pk>[0-9]+)$', 'person_detail', name='person_detail'),
)
