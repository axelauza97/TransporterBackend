# Use include() to add paths from the appVehicular
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url, handler404
from appVehicular import views
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'service',views.ServiceView,basename='service')
router.register(r'company',views.CompanyView,basename='company')
router.register(r'driver',views.DriverView,basename='driver')
router.register(r'vehicle',views.VehicleView,basename='vehicle')
router.register(r'client',views.ClientView,basename='client')
router.register(r'typeservice',views.TypeServiceView,basename='typeservice')
router.register(r'fare',views.FareView,basename='fare')
    
urlpatterns = [
    url(r'',include(router.urls)),
    url(r'^rest-auth/$',CustomAuthToken.as_view(), name ='token'),

    url(r'^login/', include('rest_social_auth.urls_token')),

    url(r'^socialauth/$', GetUserSocial.as_view()),

    url(r'^card$', Card.as_view(), name='card'),
    url(r'^transaction$', Transaction.as_view(), name='transaction'),

    url(r'^devices?$', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    url(r'^devices/delete/(?P<user>[0-9]+)/$',DeleteFCMDevice.as_view(), name ='delete_fcm_device'),
    url(r'^notification/$',NotificationFCM.as_view(), name ='NotificationFCM'),

    url(r'^acceptService/$',AcceptService.as_view(), name ='AcceptService'),
    url(r'^startService/$',StartService.as_view(), name ='StartService'),
    url(r'^endService/$',EndService.as_view(), name ='EndService'),
    url(r'^cancelService(?P<pk>[0-9]+)/$',CancelService.as_view(), name ='CancelService'),
    url(r'^recordService/(?P<pk>[0-9]+)/(?P<typee>[0-9]+)/$',RecordService.as_view(), name ='RecordService'),

    url(r'user/create/$',CreateUser.as_view()),
    url(r'user/$',UserList.as_view(),name='User'),
    url(r'user/update/(?P<pk>[0-9]+)/$', UpdateUser.as_view()),
    url(r'user/update/password/(?P<pk>[0-9]+)/$', ChangePasswordView.as_view()),

    url(r'user/(?P<pk>[0-9]+)/$', GetUser.as_view()),
    url(r'user/delete/(?P<pk>[0-9]+)/$', DeleteUser.as_view()),
    
    url(r'^getpk/(?P<user>[0-9]+)/(?P<typee>[0-9]+)/$', GetPk.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
