from ecommerce.forms import ContactoForm
from datetime import datetime
from django.templatetags.static import static
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from ecommerce.models import Cliente, Categoria, Producto, Inventario


def __buscar_categorias():
    # categorias = ["lirio", "frutales","gromineas","herramientas", "macetas", "fuentes", "cactus"]
    categorias = Categoria.objects.all()
    return categorias

def __buscar_productos(cat = "todas"):
    # productos_lista = [ {"codigo" : "1lr", "nombre" : "lirio rojo", "descripcion" : "Simbolismo: Amor y Seducción", "precio" : "8500", "stock" : "15", "categoria" : "lirio", "imagen" : static('ecommerce/images/lirio_rojo.jpg')},
    #                     {"codigo" : "1lr", "nombre" : "lirio rojo", "descripcion" : "Simbolismo: Amor y Seducción", "precio" : "8500", "stock" : "15", "categoria" : "lirio", "imagen" : static('ecommerce/images/lirio_rojo.jpg')},
    #                     {"codigo" : "1lb", "nombre" : "lirio blanco", "descripcion" : "Simbolismo: Pureza y Belleza", "precio" : "8000", "stock" : "10", "categoria" : "lirio", "imagen" : static('ecommerce/images/lirio_blanco.jpg')},
    #                     {"codigo" : "1ln", "nombre" : "lirio naranja", "descripcion" : "Simbolismo: Simbolismo: Pasión", "precio" : "8000", "stock" : "10", "categoria" : "lirio", "imagen" : static('ecommerce/images/lirio_naranja.jpg')},
    #                     {"codigo" : "1fr", "nombre" : "árboles frutales", "descripcion" : "Consultar según la temporada", "precio" : "8000", "stock" : "10", "categoria" : "frutales", "imagen" : static('ecommerce/images/frutales_rojo.jpg')},
    #                     {"codigo" : "1ca", "nombre" : "cactus", "descripcion" : "fuentes de éxito personal y laboral", "precio" : "8000", "stock" : "10", "categoria" : "cactus", "imagen" : static('ecommerce/images/cactus_verde.jpg')},
    #                     {"codigo" : "1gr", "nombre" : "gromineas", "descripcion" : "plantita espetacular para decorar", "precio" : "8000", "stock" : "10", "categoria" : "gromineas", "imagen" : static('ecommerce/images/gromineas1.jpg')},
    #                     {"codigo" : "1fu", "nombre" : "fuentes", "descripcion" : "contamos con distintos modelos", "precio" : "8000", "stock" : "10", "categoria" : "fuentes", "imagen" : static('ecommerce/images/fuente_jardin.jpg')},
    #                     {"codigo" : "1ma", "nombre" : "macetas", "descripcion" : "variedad en colores y modelos", "precio" : "8000", "stock" : "10", "categoria" : "macetas", "imagen" : static('ecommerce/images/maceta_roja.jpg')}, 
    #                     {"codigo" : "1he", "nombre" : "herramientas", "descripcion" : "Palas, regaderas, mangueras y mas", "precio" : "8000", "stock" : "10", "categoria" : "herramientas", "imagen" : static('ecommerce/images/herramientas.jpg')},]
    if cat == "todas":
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(categoria = cat)
    productos_lista = []
    for prod in productos:
        productos_lista.append({"codigo":prod.codigo, "nombre":prod.nombre, "descripcion":prod.descripcion, "precio":prod.precio, "stock":prod.cantidad, "categoria":prod.categoria, "imagen":prod.imagen})
    return productos_lista
    

# Create your views here.
def secciones(request, seccion = ''):
    formulario_contacto = ContactoForm()
    if seccion == 'contacto'and request.method == 'POST':
            formulario_contacto = ContactoForm(request.POST)
            if formulario_contacto.is_valid():
                #Si el formulario pasa las validaciones lo procesamos acá
                #enviamos mensaje formulario correcto
                messages.success(request, 'Su consulta se proceso correctamente.')
                seccion=''
                formulario_contacto = ContactoForm()
            else:
                messages.error(request, 'Su consulta NO se pudo procesar. Completala otra vez.')

    context = { "seccion": seccion,
                "ahora": datetime.now,
                "formulario_contacto": formulario_contacto,
                "productos_index" : __buscar_productos(),}
    return render(request, "index.html", context)
    

def productos(request):

    context = {"ahora":datetime.now,
               "productos": __buscar_productos()
              }
    return render(request,"productos.html", context)


def producto_categoria(request, categoria):

    context = {"ahora":datetime.now,
               "productos":__buscar_productos(categoria),
               "categorias": __buscar_categorias(),
               "activo": categoria,}
    return render(request, "productos.html", context)


def login(request):

    context = {"ahora":datetime.now}
    return render(request, "login.html", context)

