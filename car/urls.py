from django.urls import path

from . import views
app_name = "car"
urlpatterns = [
    path('', views.home, name='home'),
    path("cars/", views.car, name="car"),
    path('cars/single/<slug:slug>', views.single, name="single"),
]