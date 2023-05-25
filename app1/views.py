from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cool(request):
    return HttpResponse('<h1><b>I"m a devil of my world!!!</b></h1>')

def hot(request):
    return HttpResponse('<center><h1><marquee>This is Mr.Cool</marquee></h1></center>')