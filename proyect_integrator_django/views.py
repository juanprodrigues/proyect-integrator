from django.shortcuts import render 
from django.http import HttpResponse

from django.contrib.auth.models import User


def inicio(request):
    return render(request, 'index.html')

def acerca_de(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contact.html')