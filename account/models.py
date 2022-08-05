
from django.db import models
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.utils.translation import gettext_lazy as _


# custom user model manager
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

    # override create_superuser and create user
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
# credit card model


# custom user model


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
        return self.username + ", " + self.first_name + ", " + self.last_name

    # required methods for costum User model

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True


class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, blank=False, null=False)

    @classmethod
    def create(cls, cc_number, cc_expiry, cc_code, user):
        payment = cls(cc_number=cc_number,
                      cc_expiry=cc_expiry,
                      cc_code=cc_code, user=user)
        return payment

    def __str__(self):
        return self.user.username + " " + self.cc_number
