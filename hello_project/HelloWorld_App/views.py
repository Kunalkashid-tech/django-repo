from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sayHello(request):
    return HttpResponse('<h1 style="color:red">My First Project in Django at Aurora web LAbs.</h1>')