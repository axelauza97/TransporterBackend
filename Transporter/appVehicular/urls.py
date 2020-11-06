# Use include() to add paths from the appVehicular
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url, handler404
from appVehicular import views
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet



urlpatterns = [
    url(r'^rest-auth/$',CustomAuthToken.as_view(), name ='token'),

    url(r'^login/', include('rest_social_auth.urls_token')),

    url(r'^devices?$', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    url(r'^message/$',MessageFCM.as_view(), name ='MessageFCM'),


    url(r'user/create/$',CreateUser.as_view()),
    url(r'user/$',UserList.as_view(),name='User'),
    url(r'user/update/(?P<pk>[0-9]+)/$', UpdateUser.as_view()),
    url(r'user/(?P<pk>[0-9]+)/$', GetUser.as_view()),
    url(r'user/delete/(?P<pk>[0-9]+)/$', DeleteUser.as_view()),

    url(r'^company/$', CompanyList.as_view(), name ='company'),
    url(r'^company/(?P<pk>[0-9]+)/$', CompanyDetail.as_view()),

    url(r'^driver/$',DriverList.as_view(), name ='driver'),
    url(r'^driver/(?P<pk>[0-9]+)/$', DriverDetail.as_view()),

    url(r'^client/$',ClientList.as_view(), name ='client'),
    url(r'^client/(?P<pk>[0-9]+)/$', ClientDetail.as_view()),

    url(r'^service/$',ServiceList.as_view(), name ='service'),
    url(r'^service/(?P<pk>[0-9]+)/$', ServiceDetail.as_view()),

    url(r'^typeservice/$',TypeServiceList.as_view(), name ='typeservice'),
    url(r'^typeservice/(?P<pk>[0-9]+)/$', TypeServiceDetail.as_view()),

    url(r'^fare/$',FareList.as_view(), name ='fare'),
    url(r'^fare/(?P<pk>[0-9]+)/$', FareDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)