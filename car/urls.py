from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views
app_name = "car"
urlpatterns = [
    path('', views.home, name='home'),
    path("cars/", views.car, name="car"),
    path('cars/single/<slug:slug>', views.single, name="single"),
    path('cars/search/', views.searchByMake, name="search_make"),
]


urlpatterns += staticfiles_urlpatterns()
