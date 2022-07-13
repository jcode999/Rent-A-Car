from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    top = "This is the main page"
    return render(request,
    'home.html', {
        "top": top
    })

def car(request):
    name = "This is the cars home page"
    return render(request,
    'carshome.html', {
        "name": name
    })
