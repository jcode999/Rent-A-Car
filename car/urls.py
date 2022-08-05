from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views
app_name = "car"
urlpatterns = [
    path('', views.car, name='car'),
    path("cars/", views.car, name="car"),
    path('cars/single/<slug:slug>', views.single, name="single"),
    path('cars/search/make', views.searchByMake, name="search_make"),
    path('cars/search/model', views.searchByModel, name="search_model"),
]


urlpatterns += staticfiles_urlpatterns()
