from django.contrib import admin
from .models import Vehicle, Reservation
from account.models import Account, Payment


admin.site.register(Vehicle)
admin.site.register(Account)
admin.site.register(Reservation)
admin.site.register(Payment)

# Register your models here.
