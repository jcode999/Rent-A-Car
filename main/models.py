from django.db import models
from django.urls import reverse


class Vehicle(models.Model):
    make = models.CharField('Vehicle Make', max_length=50)
    mod = models.CharField('Vehicle Model', max_length=50)
    year = models.CharField('Vehicle Year', max_length=50)
    price = models.CharField('Vehicle Price', max_length=50, default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default="images/default.png")
    slug = models.SlugField(max_length=255, default=0)


def get_absolute_url(self):
    return reverse("main:single", args=[self.slug])


def __str__(self):
    return self.name


class RentACarUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')


def __str__(self):
    return self.first_name + ' ' + self.last_name
