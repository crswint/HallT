from django.conf.urls import patterns, include, url
from apps.tran_maps import json_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'route$', json_views.RouteCollection.as_view(), name='routes'),
    url(r'stop$', json_views.StopCollection.as_view(), name='stops'),
    url(r'route/(?P<route>\w+)/stops$', json_views.RouteStopsCollection.as_view(), name='route_stops'),
)
