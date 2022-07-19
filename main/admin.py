from django.contrib import admin
from .models import Vehicle
from .models import RentACarUser
from Account.models import Account

admin.site.register(Vehicle)
admin.site.register(RentACarUser)
admin.site.register(Account)
# Register your models here.
