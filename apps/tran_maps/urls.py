from django.conf.urls import patterns, include, url
from apps.tran_maps import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', views.MainView.as_view()),
    url(r'^onenorth/', views.OneNorth.as_view(), name='onenorth'),
    url(r'^onesouth/', views.OneSouth.as_view(), name='onesouth'),
    url(r'^two/', views.Two.as_view(), name='two'),
    url(r'^three/', views.Three.as_view(), name='three'),
    url(r'^four/', views.Four.as_view(), name='four'),
    url(r'^fivea/', views.FiveA.as_view(), name='fivea'),
    url(r'^fiveb/', views.FiveB.as_view(), name='fiveb'),
    url(r'^six/', views.Six.as_view(), name='six'),
    url(r'^all_routes/', views.AllRoutes.as_view(), name='all_routes'),

)
