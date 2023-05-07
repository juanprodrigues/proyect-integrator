from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Contacto
from django.contrib import messages
from . import models


def inicio(request):
    producto = models.Producto(nombre='A1', descripcion='Esta es una descripción de ejemplo.', precio=9.99)
    print(producto.nombre)
    # producto.save()
    return render(request, 'index.html')

def acerca_de(request):
    return render(request, 'about.html')


def contacto(request):
    if request.method == "POST":
        contacto_form = Contacto(request.POST)
        print("Este formulario esta OK?: ",contacto_form.is_valid())

        if contacto_form.is_valid():
            print("validando correo")
            print(contacto_form.cleaned_data['mail'])
            return render(request,'email_enviado.html')
    else:
        # GET
        print("contacto_form.is_valid()")
        contacto_form = Contacto()
    
    context = {
        'form': contacto_form
    }

    return render(request, 'contact.html', context)


# def contacto(request):
#     return render(request, 'contact.html')

def buscar_productos(request):
    query = request.GET.get('q')
    productos=[]
    print(not query)
    if query:
        producto = models.Producto(nombre=query, descripcion='Esta es una descripción de ejemplo.', precio=9.99)
        producto.imagen="https://i.pinimg.com/originals/1c/ee/d0/1ceed098558380f5c4739bb878bd7bce.png"
        productos.append(producto)  
    return render(request, 'productos/busqueda.html', {'productos': productos})

def crear_producto(request):
    producto = models.Producto(nombre='Producto de ejemplo', descripcion='Esta es una descripción de ejemplo.', precio=9.99)
    producto.save()
    return render(request, 'crear_producto.html', {'producto': producto})

def email_enviado(request):
    return render(request, 'email_enviado.html')
