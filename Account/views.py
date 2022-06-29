from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def testFun(request):
    html = "<html><body><H2> Accounts App <H2/></body></head>"
    return HttpResponse(html)