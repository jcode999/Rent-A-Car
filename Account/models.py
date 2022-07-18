
from django.db import models
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Email is required to create an account")
        if not first_name:
            raise ValueError("First name is required to create an account")
        if not last_name:
            raise ValueError("Last name is required to create an account")
        if not username:
            raise ValueError("username is required and must be unique")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(
        verbose_name='username', max_length=20, unique=True)
    # require fields for custom User model

    date_joined = models.DateTimeField(
        verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'  # used to log in
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = CustomAccountManager()

    def __str__(self):
        return self.username + ", " + self.first_name + ", " + self.last_name + ", "+self.email + ", " + self.password

    # required methods for costum User model

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True

class Payment(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    