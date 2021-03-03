from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class Company(models.Model):
    idCompany = models.AutoField(primary_key=True)
    nameCompany = models.CharField(max_length=45, blank=True, null=True)
    typeCompany = models.CharField(max_length=45, blank=True, null=True)
    addressCompany = models.CharField(max_length=45, blank=True, null=True)
    webpageCompany = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s: %s %s %s %s' % (self.idCompany, self.nameCompany, self.typeCompany, self.addressCompany, self.webpageCompany)

class User(AbstractUser):
    uid = models.CharField(max_length=150,unique=True)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=False,unique=True)
    cedula = models.CharField(unique=True, max_length=10, null=True)
    celular = models.CharField(max_length=10, null=True)
    #image = models.FileField(blank=True, null=True, upload_to='profiles')
    image = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Chat(models.Model):
    typee = models.CharField(max_length=200)
    userID1 = models.ForeignKey(User, related_name="userID1", blank=True, on_delete=models.CASCADE)
    userID2 = models.ForeignKey(User, related_name="userID2",blank=True, on_delete=models.CASCADE)
    date = models.DateField()
    
class Message(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, blank=True, on_delete=models.CASCADE)
    sendDate = models.DateField()
    content = models.CharField(max_length=200)
    
class Employee(models.Model):
    user = models.ManyToManyField(User, blank=True)
    
class Suggestion(models.Model):
    email = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    atendido = models.BooleanField()
    image = models.CharField(max_length=255, null=True)
    tipo = models.BooleanField(blank=True, null=True)
    
class Driver(models.Model):
    idDriver = models.AutoField(primary_key=True)
    userDriver = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    companyDriver = models.ForeignKey(Company, models.DO_NOTHING, db_column='idCompany',null=True)
    birthdateDriver = models.DateTimeField(blank=True, null=True)
    sexDriver = models.CharField(max_length=10, blank=True, null=True)
    addressDriver = models.CharField(max_length=100, blank=True, null=True)
    cipictureDriver = models.CharField(max_length=1000, blank=True, null=True) # cedula foto
    licenceDriver = models.CharField(max_length=1000, blank=True, null=True) #licencia foto
    rateDriver = models.IntegerField(blank=True, null=True)
    stateDriver = models.BooleanField(default=False) # habilitado inhabilitado
    activeDriver = models.BooleanField(default=False) # REgistrar en el sistema
    #old vehicleDriver
    class Meta:
        db_table = 'drive'
        managed = True

    def __str__(self):
       return '%s: %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.idDriver, self.userDriver,self.emailDriver,
       self.companyDriver,self.ciDriver, self.nameDriver, self.lnameDriver, self.birthdateDriver,
       self.sexDriver, self.addressDriver, self.phoneDriver, self.cipictureDriver, self.licenceDriver,
       self.rateDriver, self.stateDriver, self.activeDriver)

class TypeService(models.Model):
    idTypeService = models.AutoField(primary_key=True)
    nameTypeService = models.CharField(max_length=45, blank=True, null=True)
    descriptionTypeService = models.CharField(max_length=200, blank=True, null=True)

    
    def __str__(self):
       return '%s: %s %s' % (self.idTypeService, self.nameTypeService, self.descriptionTypeService)

#Mejora futura que se pueda selc lista vehiculos
class Vehicle(models.Model):
    idVehicle = models.AutoField(primary_key=True)
    userVehicle = models.ForeignKey(Driver, models.DO_NOTHING, db_column='idDriver',null=True)
    plateVehicle = models.CharField(max_length=10, blank=True, null=True)
    brandVehicle = models.CharField(max_length=45, blank=True, null=True)
    modelVehicle = models.CharField(max_length=45, blank=True, null=True)
    yearVehicle = models.IntegerField(blank=True, null=True)
    colorVehicle = models.CharField(max_length=45, blank=True, null=True)
    registrationVehicle = models.CharField(max_length=1000, blank=True, null=True) #matricula foto
    plpictureVehicle = models.CharField(max_length=1000, blank=True, null=True) #placa foto
    pictureVehicle = models.CharField(max_length=1000, blank=True, null=True) #vehiculo foto
    typeServiceVehicle = models.ForeignKey(TypeService, models.DO_NOTHING, db_column='idTypeService',null=True)
    typeVehicle = models.CharField(max_length=45, blank=True, null=True)
    #Old brandVehicle,typeVehicle,modelVehicle,colorVehicle
    class Meta:
        db_table = 'vehicle'
        managed = True

    def __str__(self):
        return '%s: %s %s %s %s %s %s %s %s %s %s %s' % (self.idVehicle,self.userVehicle, self.brandVehicle, self.plateVehicle,
        self.modelVehicle, self.yearVehicle, self.colorVehicle, self.registrationVehicle, self.pictureVehicle,
        self.plpictureVehicle,self.typeServiceVehicle, self.typeVehicle)

class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    userClient = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
       return '%s: %s %s' % (self.idClient, self.userClient, self.rateClient)

class Fare(models.Model):
    idFare = models.AutoField(primary_key=True)
    idCompanyFare = models.ForeignKey(Company, models.DO_NOTHING, db_column='idCompany',null=True)
    idTypeServiceFare = models.ForeignKey(TypeService, models.DO_NOTHING, db_column='idTypeService')
    minFare = models.FloatField(blank=True, null=True)
    priceFare = models.FloatField(blank=True, null=True)

    
    def __str__(self):
       return '%s: %s %s %s %s' % (self.idFare, self.idCompanyFare, self.idTypeServiceFare, self.minFare, self.priceFare)

class Payment(models.Model):
    idPayment = models.AutoField(primary_key=True)
    nameTypeService = models.CharField(max_length=45, blank=True, null=True)
    descriptionTypeService = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.nameTypeService)


class Service(models.Model):
    states =( 
    (0, "UNASSIGNED"), 
    (1, "ASSIGNED"),
    (2, "EN CURSO"),
    (3, "FINALIZADO"),
    (4, "CANCELED")
    ) 
    idService = models.AutoField(primary_key=True)
    idClientService = models.ForeignKey(Client, models.DO_NOTHING, db_column='idClient')
    idDriverService = models.ForeignKey(Driver, models.DO_NOTHING, db_column='idDriver',blank=True, null=True)
    #coordenada
    coordStart = models.CharField(max_length=200, blank=True, null=True)
    coordEnd = models.CharField(max_length=200, blank=True, null=True)
    #nombre
    startAddress=models.CharField(max_length=200, blank=True, null=True)
    endAddress=models.CharField(max_length=200, blank=True, null=True)
    
    idTypePaymentService = models.ForeignKey(Payment, models.DO_NOTHING, db_column='idPayment')
    idTypeService = models.ForeignKey(TypeService, models.DO_NOTHING, db_column='idTypeService')
    driverScore = models.IntegerField(blank=True, null=True)
    clientScore = models.IntegerField(blank=True, null=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    isReservationService = models.BooleanField(blank=True, null=True)
    stateService = models.IntegerField(choices=states, default=0)
    amountPayment = models.FloatField(blank=True, null=True)
    tokenPayment = models.CharField(max_length=200, blank=True, null=True)

    
    def __str__(self):
       return '%s: %s %s' % (self.idService, self.startDate, self.endDate)


class Details(models.Model):
    service = models.ForeignKey(Service, blank=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=25)
    
