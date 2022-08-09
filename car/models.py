from django.db import models
from django.urls import reverse
from account.models import Account
from django.utils.translation import gettext_lazy as _
import datetime


class Vehicle(models.Model):
    make = models.CharField('Vehicle Make', max_length=50)
    mod = models.CharField('Vehicle Model', max_length=50)
    year = models.CharField('Vehicle Year', max_length=50)
    mile = models.CharField('Vehicle mile', max_length=50, default="")
    trans = models.CharField('Vehicle trans', max_length=50, default="")
    body = models.CharField('Vehicle type', max_length=50, default="")
    color = models.CharField('Vehicle color', max_length=50, default="")
    price = models.DecimalField(
        'Vehicle Price', max_digits=5, decimal_places=2)
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


class Reservation(models.Model):
    renter = models.ForeignKey(
        Account, on_delete=models.CASCADE, blank=False, null=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True,
                                null=True)
    reservation_date = models.DateField(
        _("Reservation date"), default=datetime.date.today)
    return_date = models.DateField(
        _("Return date"), default=datetime.date.today)

    @classmethod
    def create(cls, renter, vehicle, reservation_date, return_date):
        reservation = cls(renter=renter, vehicle=vehicle,
                          reservation_date=reservation_date, return_date=return_date)
        return reservation

    def __str__(self):
        return self.renter.username
