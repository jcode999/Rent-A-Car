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
    if request.method == 'GET':
        return render(request, 'searches/search_by_make.html')
    return render(request, 'searches/search_by_make.html')
