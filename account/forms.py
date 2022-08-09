from django import forms
from django.forms import ModelForm
from account.models import Account, Payment
from django.contrib.auth.forms import UserCreationForm
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

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


class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'return_date']
