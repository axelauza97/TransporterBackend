from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Company)
admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Client)
admin.site.register(TypeService)
admin.site.register(Fare)
admin.site.register(Payment)
admin.site.register(Location)
admin.site.register(Service)

