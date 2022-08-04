from pickletools import opcodes
from django.db import models
from django.urls import reverse
from account.models import Account


class Vehicle(models.Model):
    make = models.CharField('Vehicle Make', max_length=50)
    mod = models.CharField('Vehicle Model', max_length=50)
    year = models.CharField('Vehicle Year', max_length=50)
    price = models.CharField('Vehicle Price', max_length=50, default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default="images/default.png")
    slug = models.SlugField(max_length=255, default=0)
    licensePlate = models.CharField(max_length=8)
    current_inventory = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("car:single", args=[self.slug])

    def __str__(self):
        return self.make


class Reservation(models.Model):
    renter = models.ForeignKey(
        Account, on_delete=models.CASCADE, blank=False, null=False)
    vehicle = models.ManyToManyField(Vehicle)
