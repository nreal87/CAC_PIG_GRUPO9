from ecommerce.forms import ContactoForm, ProductoForm
from datetime import datetime
from django.templatetags.static import static
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from ecommerce.models import Cliente, Categoria, Producto, Inventario



def __buscar_categorias():
    #categorias = ["lirio", "frutales","gromineas","herramientas", "macetas", "fuentes", "cactus"]
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
       #productos = Producto.objects.filter(categoria = cat)
       #Consultar si hay una mejor forma de hacer esta consulta
       consulta_categoria = Categoria.objects.filter(nombre = cat)
       productos = Producto.objects.filter(categoria = consulta_categoria[0].id) 

    productos_lista = []
    for prod in productos:
        # productos_lista.append({"codigo":prod.codigo, "nombre":prod.nombre, "descripcion":prod.descripcion, "precio":prod.precio, "stock":prod.cantidad, "categoria":prod.categoria, "imagen":prod.imagen}) # Para que ande la imagen posiblemente haga falta otra dependencia
        productos_lista.append({"codigo":prod.codigo, "nombre":prod.nombre, "descripcion":prod.descripcion, "precio":prod.precio, "stock":"1", "categoria":prod.categoria, "imagen": prod.imagen})
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
               "productos": __buscar_productos(),
               "categorias": __buscar_categorias(),
              }
    return render(request,"productos.html", context)


def producto_categoria(request, categoria):
    context = {"ahora":datetime.now,
               "productos":__buscar_productos(categoria),
               "categorias": __buscar_categorias(),
               "activo": categoria,}
    return render(request, "productos.html", context)


# En esta vista deberiamos manejar la visualizacion del carrito del usuario con los productos elegidos, cantidades, precios y total
def ver_carrito(request):
    context = {"ahora":datetime.now,
               "productos": __buscar_productos()
              }
    return render(request,"carrito.html", context)


# En esta vista deberiamos manejar la validacion de la compra del carrito y mostrar un mensaje de exito o error en la operacion
def comprar_carrito(request):
    context = {"ahora":datetime.now,
               "productos": __buscar_productos()
              }
    return render(request,"compra.html", context)


# A implementar luego cuando veamos como lo resuelve Django
def login(request):

    context = {"ahora":datetime.now}
    return render(request, "login.html", context)


# Esta vista permite crear mas facil todas las instancias que deben existir en la db inicialmente
def iniciar_db(request):
    # Creacion de categorias
    Categoria1 = Categoria(nombre="Lirio", descripcion="Categoria Lirio")
    Categoria2 = Categoria(nombre="Frutales", descripcion="Categoria Frutales")
    Categoria3 = Categoria(nombre="Cactus", descripcion="Categoria Cactus")
    Categoria4 = Categoria(nombre="Gromineas", descripcion="Categoria Gromineas")
    Categoria5 = Categoria(nombre="Fuentes", descripcion="Categoria Fuentes")
    Categoria6 = Categoria(nombre="Macetas", descripcion="Categoria Macetas")
    Categoria7 = Categoria(nombre="Herramientas", descripcion="Categoria Herramientas")
    Categoria1.save()
    Categoria2.save()
    Categoria3.save()
    Categoria4.save()
    Categoria5.save()
    Categoria6.save()
    Categoria7.save()
    # Creacion de productos
    Producto1 = Producto(codigo="1lr", nombre="lirio rojo", descripcion="Simbolismo: Amor y seducción", precio=8500.0, categoria_id=Categoria1.id)
    Producto2 = Producto(codigo="1lb", nombre="lirio blanco", descripcion="Simbolismo: Pureza y belleza", precio=8000.0, categoria_id=Categoria1.id)
    Producto3 = Producto(codigo="1ln", nombre="lirio naranja", descripcion="Simbolismo: Pasion", precio=8000.0, categoria_id=Categoria1.id)
    Producto4 = Producto(codigo="1fr", nombre="arboles frutales", descripcion="Consultar segun la temporada", precio=8000.0, categoria_id=Categoria2.id)
    Producto5 = Producto(codigo="1ca", nombre="cactus", descripcion="Fuentes de exito personal y laboral", precio=8000.0, categoria_id=Categoria3.id)
    Producto6 = Producto(codigo="1gr", nombre="gromineas", descripcion="Plantita espectacular para decorar", precio=8000.0, categoria_id=Categoria4.id)
    Producto7 = Producto(codigo="1fu", nombre="fuentes", descripcion="Contamos con distintos modelos", precio=8000.0, categoria_id=Categoria5.id)
    Producto8 = Producto(codigo="1ma", nombre="macetas", descripcion="Variedad de colores y modelos", precio=8000.0, categoria_id=Categoria6.id)
    Producto9 = Producto(codigo="1he", nombre="herramientas", descripcion="Palas, regaderas, mangueras y mas", precio=8000.0, categoria_id=Categoria7.id)
    Producto1.save()
    Producto2.save()
    Producto3.save()
    Producto4.save()
    Producto5.save()
    Producto6.save()
    Producto7.save()
    Producto8.save()
    Producto9.save()
    return redirect("secciones")


def crear_producto(request):
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto guardado.')
            # return redirect('productos')
    
    context = { "ahora": datetime.now,
                "formulario_producto": ProductoForm(),
            }
    return render(request, "crear_producto.html", context)