from django.urls import path

from . import views
app_name = "main"
urlpatterns = [
    path('', views.home, name='home'),
    path("cars/", views.car, name="car"),
    path('single/<slug:slug>', views.single, name="single"),
]