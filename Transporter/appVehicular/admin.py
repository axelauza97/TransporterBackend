from django.contrib import admin
from .models import *
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.


TokenAdmin.raw_id_fields = ['user']
admin.site.register(Company)
admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Client)
admin.site.register(TypeService)
admin.site.register(Fare)
admin.site.register(Payment)
admin.site.register(Location)
admin.site.register(Service)
admin.site.register(Police)
admin.site.register(Manager)
