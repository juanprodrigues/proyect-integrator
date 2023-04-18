from django.shortcuts import render 
from django.http import HttpResponse

from . import models



# from django.contrib.auth.models import User

# Create user and save to the database

# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again

# user.first_name = 'John'
# user.last_name = 'Citizen'
# user.save()

def inicio(request):
    producto = models.Producto(nombre='A1', descripcion='Esta es una descripción de ejemplo.', precio=9.99)
    print(producto.nombre)
    # producto.save()
    return render(request, 'index.html')

def acerca_de(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contact.html')

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