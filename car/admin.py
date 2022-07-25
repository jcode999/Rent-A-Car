from django.contrib import admin
from .models import Vehicle, Reservation
from account.models import Account


admin.site.register(Vehicle)
admin.site.register(Account)
admin.site.register(Reservation)
# Register your models here.
