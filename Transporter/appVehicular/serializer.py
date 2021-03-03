from .models import *
from rest_framework import serializers
from .firebase import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    uid = serializers.CharField(required=False)
    def create(self, validated_data):
        cedula = validated_data['cedula']
        email = validated_data['email']
        celular = validated_data['celular']
        image = validated_data['image']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password=validated_data['password']
        uid = crearUsuarioFirebase(email,first_name,last_name)
        if (not uid is  None):
            user = User.objects.create(
                uid=uid,
                cedula = cedula,
                email = email,
                celular = celular,
                image = image,
                first_name = first_name,
                last_name = last_name,
                )
            user.set_password(validated_data['password'])
            user.save()
            return user
        else:
            print("error")
            return None
        

    class Meta:
        model = User
        fields = (
            'id',
            'uid',
            'cedula',
            'password',
            'email',
            'celular',
            'email',
            'image',
            'first_name',
            'last_name',
            'is_active',
        )


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
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

class ClientSerializerShow(serializers.ModelSerializer):
    userClient=UserSerializer()
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

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceSerializerShow(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        depth = 1


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'