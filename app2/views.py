from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def simha(request):
    return HttpResponse('<h1><b>I"m the KING of own KINGDOM!!!</b></h1>')

def reddy(request):
    return HttpResponse('<center><h1><marquee>This is Mr.IPL</marquee></h1></center>')