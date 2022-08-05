from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle
# Create your views here.


def home(request):
    message = "This is the main page"
    return render(request,
                  'home.html', {
                      "message": message
                  })


def car(request):
    vehicle_list = Vehicle.objects.all()
    return render(request, 'carshome.html', {'vehicle_list': vehicle_list})


def single(request, slug):
    data = Vehicle.objects.get(slug=slug)
    return render(request, "single.html", {"vehicle": data})


def searchByMake(request):
    make = request.GET.get('make')
    make_list = Vehicle.objects.filter(make=make)
    return render(request, 'searches/search_by_make.html', {'make_list': make_list})


def searchByModel(request):
    model = request.GET.get('model')
    model_list = Vehicle.objects.filter(mod=model)
    return render(request, 'searches/search_by_model.html', {'model_list': model_list})
