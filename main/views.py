from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle
# Create your views here.


def index(request):
    top = "This is the main page"
    return render(request,
                  'home.html', {
                      "top": top
                  })


def car(request):
    vehicle_list = Vehicle.objects.all()
    return render(request,
                  'carshome.html',
                  {
                      'vehicle_list': vehicle_list
                  })
