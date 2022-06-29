from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def logoDisplay(request):
    html = "<html><body><H2> Rent-A-Car<H2/></body></head>"
    return HttpResponse(html)
    
