from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {'password':{'write_only':True}}
    def crate(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        user = User(email,username)
        user.set_password(validated_data['password'])
        user.save()
        #lista = []
        #lista.append(email)
        desde = settings.EMAIL_HOST_USER
        asunto = "Beinvenido a Transporter"
        #link
        contenido = "<p>\nEstos son tus datos para login: \n</p><p>email: %s \nContrasena: %s \n</p>" % (email,password)
        #mail = EmailMessage(asunto, contenido, desde, lista)
        #mail.content_subtype = "html"
        #mail.send()
        send_mail(asunto, contenido, desde, email)
        return user

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class TypeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeService
        fields = '__all__'

class FareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fare
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Police
        fields = '__all__'
