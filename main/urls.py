from django.urls import path

from . import views
app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path("cars/", views.car, name="car"),
    path('single/<slug:slug>', views.single, name="single"),
]
