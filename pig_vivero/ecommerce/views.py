from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)

def productos(request):
    context = {}
    return render(request,"productos.html", context)

def producto_categoria(request, categoria):
    context = {'categoria' : categoria,}
    return render(request, "productos.html", context)

def login(request):
    context = {}
    return render(request, "login.html", context)

def secciones(request, seccion):
    direccion = f'/#{seccion}'
    return redirect(direccion)


