from django import forms
from django.forms import ModelForm
from account.models import Account, Payment
from django.contrib.auth.forms import UserCreationForm

from car.models import Reservation


class LogInForm(forms.Form):
    username = forms.CharField(max_length=50, label='username')
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateUserForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name']


class PaymentForm(ModelForm):

    class Meta:
        model = Payment
        fields = ['cc_number', 'cc_expiry', 'cc_code']


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'return_date']
