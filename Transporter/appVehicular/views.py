from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import *
from .serializer import *
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import permissions

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]

# Create your views here.
#get, post
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

#update, delete
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


#get, post
class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

#update, delete
class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


#get, post
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

#update, delete
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#get, post
class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

#update, delete
class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

#get, post
class TypeServiceList(generics.ListCreateAPIView):
    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

#update, delete
class TypeServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer

#get, post
class FareList(generics.ListCreateAPIView):
    queryset = Fare.objects.all()
    serializer_class = FareSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

#update, delete
class FareDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fare.objects.all()
    serializer_class = FareSerializer
