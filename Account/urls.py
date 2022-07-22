from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logIn, name='login'),
    path('registration/', views.registration, name='registration'),
    path('dashboard/<username>/', views.dashboard, name='dashboard')

]
