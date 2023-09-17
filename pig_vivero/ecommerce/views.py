from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)

def styles(request):
    context = {}
    return render(request, "assets/css/styles.css", context)

def productos(request):
    context = {}
    return render(request,"productos.html", context)

def producto_categoria(request, categoria):
    context = {'categoria' : categoria,}
    return render(request, "productos.html", context)

def login(request):
    context = {}
    return render(request, "login.html", context)