from pickletools import opcodes
from django.db import models
from django.urls import reverse
from account.models import Account


class Vehicle(models.Model):
    make = models.CharField('Vehicle Make', max_length=50)
    mod = models.CharField('Vehicle Model', max_length=50)
    year = models.CharField('Vehicle Year', max_length=50)
    mile = models.CharField('Vehicle mile', max_length=50, default="")
    trans = models.CharField('Vehicle trans', max_length=50, default="")
    body = models.CharField('Vehicle type', max_length=50, default="")
    color = models.CharField('Vehicle color', max_length=50, default="")
    price = models.IntegerField('Vehicle Price', default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default="images/default.png")
    interiorImage = models.ImageField(
        upload_to="images/", default="images/default.png")
    secondaryImage = models.ImageField(
        upload_to="images/", default="images/default.png")
    slug = models.SlugField(max_length=255, default=0)

    def get_absolute_url(self):
        return reverse("car:single", args=[self.slug])

    def __str__(self):
        return self.make
