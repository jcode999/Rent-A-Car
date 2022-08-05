from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logIn, name='login'),
    path('registration/', views.registration, name='registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.log_out, name='logout'),
    path('dashboard/payment', views.add_credit_card, name='add_payment'),
    path('dashboard/update', views.update_info, name='update_info'),


]
