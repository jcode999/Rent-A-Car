from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    bodyStyle = models.CharField(max_length=20)
    # ToDo change to proper fielType
    year = models.CharField(max_length = 20) 
    rentCharge = models.PositiveIntegerField()
    inventory = models.PositiveBigIntegerField()

    #test
    def __str__(self):
        info = self.make +'\n' + self.model +'\n' + self.year +'\n' +self.bodyStyle +'\n' + self.rentCharge+'\n'+self.inventory
        return info


