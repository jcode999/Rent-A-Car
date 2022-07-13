from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
    return HttpResponse("<h1>Hello This is the Home page!</h1>")


#def car(response):
 #   return HttpResponse("<h1> {{ name }} </h1>")

def car(request):
    name = "This is the cars home page"
    return render(request,
    'home.html', {
        "name": name
    })
