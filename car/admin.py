from django.contrib import admin
from .models import Vehicle
from account.models import Account


admin.site.register(Vehicle)
admin.site.register(Account)

# Register your models here.
