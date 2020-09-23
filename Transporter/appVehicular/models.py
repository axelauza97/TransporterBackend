from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    idCompany = models.AutoField(primary_key=True)
    nameCompany = models.CharField(max_length=45, blank=True, null=True)
    typeCompany = models.CharField(max_length=45, blank=True, null=True)
    addressCompany = models.CharField(max_length=45, blank=True, null=True)
    webpageCompany = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'company'
        managed = True

    def __str__(self):
        return '%s: %s %s %s %s' % (self.idCompany, self.nameCompany, self.typeCompany, self.addressCompany, self.webpageCompany)

class Vehicle(models.Model):
    idVehicle = models.AutoField(primary_key=True)
    brandVehicle = models.CharField(max_length=45, blank=True, null=True)
    typeVehicle = models.CharField(max_length=45, blank=True, null=True)
    modelVehicle = models.CharField(max_length=45, blank=True, null=True)
    colorVehicle = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'vehicle'
        managed = True

    def __str__(self):
        return '%s: %s %s %s %s' % (self.idVehicle, self.brandVehicle, self.typeVehicle, self.modelVehicle, self.colorVehicle)


class Driver(models.Model):
    idDriver = models.AutoField(primary_key=True)
    userDriver = models.OneToOneField(User, on_delete=models.CASCADE)
    rateDriver = models.IntegerField(blank=True, null=True)
    vehicleDriver = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='idVehicle')

    class Meta:
        db_table = 'drive'
        managed = True

    def __str__(self):
       return '%s: %s %s %s' % (self.idDriver, self.userDriver, self.rateDriver, self.vehicleDriver)

class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    userClient = models.OneToOneField(User, on_delete=models.CASCADE)
    rateClient = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'client'
        managed = True

    def __str__(self):
       return '%s: %s %s' % (self.idClient, self.userClient, self.rateClient)

class TypeService(models.Model):
    idTypeService = models.AutoField(primary_key=True)
    nameTypeService = models.CharField(max_length=45, blank=True, null=True)
    descriptionTypeService = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'typeService'
        managed = True

    def __str__(self):
       return '%s: %s %s' % (self.idTypeService, self.nameTypeService, self.descriptionTypeService)

class Fare(models.Model):
    idFare = models.AutoField(primary_key=True)
    idCompanyFare = models.ForeignKey(Company, models.DO_NOTHING, db_column='idCompany')
    idTypeServiceFare = models.ForeignKey(TypeService, models.DO_NOTHING, db_column='idTypeService')
    maxFare = models.IntegerField(blank=True, null=True)
    priceFare = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'fare'
        managed = True

    def __str__(self):
       return '%s: %s %s %s %s' % (self.idFare, self.idCompanyFare, self.idTypeServiceFare, self.maxFare, self.priceFare)

class Payment(models.Model):
    idPayment = models.AutoField(primary_key=True)
    idFarePayment = models.ForeignKey(Fare, models.DO_NOTHING, db_column='idFare')
    typePayment = models.CharField(max_length=45, blank=True, null=True)
    amountPayment = models.FloatField(blank=True, null=True)
    driverneedPayment = models.FloatField(blank=True, null=True)
    chargeamountPayment = models.FloatField(blank=True, null=True)
    totalPayment = models.FloatField(blank=True, null=True)
    datePayment = models.DateTimeField(blank=True, null=True)
    tokenPayment = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'payment'
        managed = True

    def __str__(self):
        return self.amountPayment

class Location(models.Model):
    idLocation = models.AutoField(primary_key=True)
    latitudeLocation = models.CharField(max_length=20, blank=True, null=True)
    longitudeLocation = models.CharField(max_length=20, blank=True, null=True)
    nameLocation = models.CharField(max_length=200, blank=True, null=True)
    tokenLocation = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'location'
        managed = True

    def __str__(self):
       return '%s: %s %s %s %s' % (self.idLocation, self.latitudeLocation, self.longitudeLocation, self.nameLocation, self.tokenLocation)

class Service(models.Model):
    idService = models.AutoField(primary_key=True)
    idClientService = models.ForeignKey(Client, models.DO_NOTHING, db_column='idClient')
    idDriverService = models.ForeignKey(Driver, models.DO_NOTHING, db_column='idDriver')
    #startidLocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='idLocation')
    endidLocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='idLocation')
    idPaymentService = models.ForeignKey(Payment, models.DO_NOTHING, db_column='idPayment')
    idTypeService = models.ForeignKey(TypeService, models.DO_NOTHING, db_column='idTypeService')
    driverScore = models.IntegerField(blank=True, null=True)
    clientScore = models.IntegerField(blank=True, null=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    isReservationService = models.BooleanField(blank=True, null=True)
    stateService = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'service'
        managed = True

    def __str__(self):
       return '%s: %s %s %s' % (self.idService, self.endidLocation, self.startDate, self.endDate)


