"""Transporter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework.authtoken import views
from django.conf import settings
from rest_framework import routers
from appVehicular.views import UserViewset
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register('users', UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api', include('appVehicular.urls')),
    url(r'^api/', include('appVehicular.urls')),
    path(r'api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),


]
