from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import *
from .serializer import *
from .forms import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import permissions
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework import viewsets

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from fcm_django.fcm import fcm_send_topic_message
from fcm_django.models import FCMDevice
import json
from django.db import transaction

from django.http import JsonResponse


"""obtener pk de client y driver por user"""



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id':user.id,
            'isAdmin': user.is_superuser,
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
        })


class NotificationFCM(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        form = NotificationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            user = form.cleaned_data['user']
            data = eval(form.cleaned_data['data'])
            print(title,body,user,json.dum(data))
            print(Driver.objects.values('userDriver'))
            notify(title,body,user,data)
            return Response({'Notification sent successfully'})
        else:
            return Response({'Notification error'})

def notify(title,body,user,data):
    if user=="0":   
        devices = FCMDevice.objects.filter(user__in=Driver.objects.values('userDriver'))
    if user=="1":   
        devices = FCMDevice.objects.filter(user__in=Client.objects.values('userClient'))
    if user=="2":   
        devices = FCMDevice.objects.filter(user__in=Employee.objects.values('user'))

    for device in devices:
        print(device)
        device.send_message(title=title, body=body,data=data)
        device.is_active=True
        device.save()


class AcceptService(APIView):
    permission_classes = (AllowAny,)
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = AcceptServiceForm(request.POST)
        if form.is_valid():
            servicePk=form.cleaned_data['service']
            user_driverPk=form.cleaned_data['driver']
            user_clientPk=form.cleaned_data['client']
            data = eval(form.cleaned_data['data'])
            service=Service.objects.get(pk=servicePk) 
            if service.stateService==0:
                device = FCMDevice.objects.get(user=user_clientPk)
                service.stateService=1
                driverPk=User.objects.get(pk=user_driverPk)
                driver=Driver.objects.get(userDriver=driverPk)      
                service.idDriverService=driver
                service.save()
                device.send_message(title="Atencion", body="Servicio Assignado",data=data)
                device.is_active=True
                device.save()
                return Response({'Servicio assignado'})
            else:
                return Response({'Servicio ya fue assignado'})
        else:
            return Response({'Error'})

class GetPk(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs,):
        user = int(kwargs.get('user', 0))
        typee = int(kwargs.get('typee', 0))
        #Driver
        if typee==0:
            pk=Driver.objects.get(userDriver=user).pk
        #Client
        elif typee==1:
            pk=Client.objects.get(userClient=user).pk
        else:
            return Response({"Error"})
        return Response({"pk":pk})

class RecordService(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs,):
        pk = int(kwargs.get('pk', 0))
        typee = int(kwargs.get('typee', 0))
        #Driver
        if typee==0:
            services=Service.objects.filter(idDriverService=pk)
        #Client
        elif typee==1:
            services=Service.objects.filter(idClientService=pk)
        else:
            return Response({"Error"})
        data = list(services.values())
        return JsonResponse(data, safe=False)  
        

class DeleteFCMDevice(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request, *args, **kwargs):
        user=kwargs.get('user', 0)
        if user==0:
            return Response({"Error"})
        devices=FCMDevice.objects.filter(user=user)
        for device in devices:
            device.delete()
        return Response({"Successful"})

#USUARIO
#--------------------------------------------------------------
class CreateUser(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

class GetUser(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

class DeleteUser(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

class UpdateUser(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully'
                }
                return Response(response)



#get, post
class CompanyList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)
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

class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

#update, delete
class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

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


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, request):
        service=self.get_serializer(data=request.data)
        if service.is_valid():
            new_service=service.save()
            dictService=request.data
            dictService['pk']=new_service.pk
            notify(title="Atencion",body="Nuevo Servicio",user="0",data=dictService)

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


