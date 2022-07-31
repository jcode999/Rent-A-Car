from django import forms
from django.forms import EmailInput
from account.models import Account
from django.contrib.auth.forms import UserCreationForm


class LogInForm(forms.Form):
    username = forms.CharField(max_length=50, label='username')
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='user name')
    email = forms.CharField(widget=EmailInput)
    first_name = forms.CharField(max_length=50, label='first_name')
    last_name = forms.CharField(max_length=50, label='last_name')
    

    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name']
