from django.db import models

class Vehicle(models.Model):
    make = models.CharField('Vehicle Make', max_length=50)
    mod = models.CharField('Vehicle Model', max_length=50)
    year = models.CharField('Vehicle Year', max_length=50)
    price = models.CharField('Vehicle Price', max_length=50)
    description = models.TextField(blank=True)

def __str__(self):
    return self.name

class RentACarUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

def __str__(self):
    return self.first_name + ' ' + self.last_name

