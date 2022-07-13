import django_on_heroku
from decouple import config

from .baseSettings import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False
ALLOWED_HOST = [
  'UNT_rentacar.herokuapp.com',
]