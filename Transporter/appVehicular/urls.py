# Use include() to add paths from the appVehicular
from .views import *
from django.conf.urls import url, handler404
from rest_framework.urlpatterns import format_suffix_patterns
from appVehicular import views

urlpatterns = [
    url(r'^company/$',CompanyList.as_view(), name ='company'),
    url(r'^company/(?P<pk>[0-9]+)/$', CompanyDetail.as_view()),

    url(r'^Manager/$',ManagerList.as_view(), name ='manager'),
    url(r'^Manager/(?P<pk>[0-9]+)/$', ManagerDetail.as_view()),

    url(r'^vehicle/$',VehicleList.as_view(), name ='vehicle'),
    url(r'^vehicle/(?P<pk>[0-9]+)/$', VehicleDetail.as_view()),

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

    url(r'^police/$',PoliceList.as_view(), name ='police'),
    url(r'^police/(?P<pk>[0-9]+)/$', PoliceDetail.as_view()),

    url('users/',UserCreate.as_view(), name='user_create'),
]
