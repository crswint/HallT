from django.conf.urls import patterns, include, url
from apps.tran_maps import views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HallT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tran_maps/', include('apps.tran_maps.urls', namespace='tran_maps'))
)
