from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import *
from .serializer import *

from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import permissions
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'isAdmin': user.is_superuser,
        })

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


from fcm_django.fcm import fcm_send_topic_message
from fcm_django.models import FCMDevice



class MessageFCM(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        devices = FCMDevice.objects.all()
        for device in devices:
            print(device)
            device.send_message(title="QUINTOO MENSAJE", body="MENSAJEEE!")
        return Response({'ddd'})


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
    permission_classes = (IsAuthenticated,)
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



