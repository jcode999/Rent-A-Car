from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=20)
    uid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        info = self.name + '\n' + self.uid + '\n' + self.password
        return info 

