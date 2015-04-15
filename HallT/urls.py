from django.conf.urls import patterns, include, url
from apps.tran_maps import views
from django.contrib import admin

api_patterns = patterns('',
    url(r'^', include('apps.tran_maps.api_urls'), name='tran_maps_api')
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HallT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tran_maps/', include('apps.tran_maps.urls', namespace='tran_maps')),
    url(r'^api/v1/', include(api_patterns, namespace='api')),

)
