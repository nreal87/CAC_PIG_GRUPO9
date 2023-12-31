from ecommerce.forms import ContactoForm
from datetime import datetime
from django.templatetags.static import static
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from administracion.models import Cliente, Categoria, Producto, Carrito, ItemCarrito
from administracion.forms import UserRegisterForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def __buscar_categorias():
    """ La funcion la usaremos para consultar el listado de categorias, 
    no retorna solo el nombre de la categoria. """
    categorias = Categoria.objects.all()
    return categorias


def __buscar_productos_categoria(cat="todas"):
    """ La funcion la usamos para obtener el listado de los productos por el tipo de categoria, 
        si le pasamos all, nos retorna un listado de todos los productos. """

    if cat == "todas":
        productos = Producto.objects.all()
    else:
        #consulta_categoria = Categoria.objects.filter(nombre=cat)
        #productos = Producto.objects.filter(categoria=consulta_categoria[0].id)
        productos = Producto.objects.filter(categoria__nombre=cat)
    
    productos_lista = []
    for prod in productos:
        productos_lista.append({"nombre": prod.nombre, "descripcion": prod.descripcion, "precio": prod.precio, "stock": prod.cantidad,
                                "categoria": prod.categoria, "imagen": prod.imagen})
    return productos_lista

def error(request):
    context = {"ahora": datetime.now}
    return render(request, "ecommerce/404.html",context)

def __buscar_productos(nombreProd=""):
    """ La funcion busca un producto por su nombre, si no le pasamos ningun nombre 
    por el cual buscar nos retornara los productos que tengan el atriburo promocion en true"""

    if nombreProd == "":
        consulta_producto = Producto.objects.filter(promocion=True)
    else:
        consulta_producto = Producto.objects.filter(nombre=nombreProd)

    productos_lista = []
    for prod in consulta_producto:
        productos_lista.append({"nombre": prod.nombre, "descripcion": prod.descripcion, "precio": prod.precio, "stock": prod.cantidad,
                                "categoria": prod.categoria, "imagen": prod.imagen, "id": prod.id})
    return productos_lista

# Create your views here.


def secciones(request, seccion=''):
    """Con esta vista nos desplazamos entre las distintas secciones del index"""

    formulario_contacto = ContactoForm()
    if seccion == 'contacto' and request.method == 'POST':
        formulario_contacto = ContactoForm(request.POST)
        if formulario_contacto.is_valid():
            # Si el formulario pasa las validaciones lo procesamos acá
            # enviamos mensaje formulario correcto
            messages.success(request, 'Su consulta se proceso correctamente.')
            seccion = ''
            formulario_contacto = ContactoForm()
        else:
            messages.error(
                request, 'Su consulta NO se pudo procesar. Completala otra vez.')
    context = {"seccion": seccion,
               "ahora": datetime.now,
               "formulario_contacto": formulario_contacto,
               "productos_index": __buscar_productos(), }
    return render(request, "ecommerce/index.html", context)


def productos(request):
    """Esta vista la usamos para cargar todos los productos en el mercado, la invocamos
    desde PRODUCTOS en la barra de navegacion"""
    context = {"ahora": datetime.now,
               "productos": __buscar_productos_categoria(),
               "categorias": __buscar_categorias(),
               }
    return render(request, "ecommerce/productos.html", context)


def producto_id(request, id_prod):
    """Esta vista la usamos para ver el producto seleccionado en el mercado, 
      la estamos invocando desde el listado de productos que se muestran en el index"""
    context = {"ahora": datetime.now,
               "productos": Producto.objects.filter(id=id_prod),
               "categorias": __buscar_categorias(),
               }
    return render(request, "ecommerce/productos.html", context)


def producto_categoria(request, categoria):
    """Esta vista nos permite mostrar en el mercado los productos de la categoria seleccionada """
    context = {"ahora": datetime.now,
               "productos": __buscar_productos_categoria(categoria),
               "categorias": __buscar_categorias(),
               "activo": categoria, }
    return render(request, "ecommerce/productos.html", context)


# En esta vista deberiamos manejar la visualizacion del carrito del usuario con los productos elegidos, cantidades, precios y total
class ProductosListView(LoginRequiredMixin,ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'ecommerce/carrito.html'
    queryset = Producto.objects.all()


# En esta vista deberiamos manejar la visualizacion del carrito del usuario con los productos elegidos, cantidades, precios y total
class CarritoListView(LoginRequiredMixin,ListView):
    model = ItemCarrito
    context_object_name = 'Carrito'
    template_name = 'ecommerce/carrito.html'
    # queryset = ItemCarrito.objects.filter(carrito=self.request.user.cliente.carrito)

@login_required(login_url="ecommerce_login")
def ver_carrito(request):
    """Esta vista nos permite mostrar los items del carrito activo del usuario """
    carrito_cliente=Carrito.objects.filter(cliente=request.user.cliente, compra_abierta=True)
    items_carrito = ItemCarrito.objects.filter(carrito=carrito_cliente[0])
    
    context = {"ahora": datetime.now,
               "items_carrito": items_carrito }
    return render(request, "ecommerce/carrito.html", context)




# En esta vista deberiamos manejar la validacion de la compra del carrito y mostrar un mensaje de exito o error en la operacion
def comprar_carrito(request):
    context = {"ahora": datetime.now,
               "productos": __buscar_productos()
               }
    return render(request, "ecommerce/compra.html", context)


# A implementar luego cuando veamos como lo resuelve Django
def ecommerce_login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bienvenido/a {username} !!')
            return redirect('secciones')
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    context = {"ahora": datetime.now,
               'form': form}
    return render(request, "ecommerce/login.html", context)

def ecommerce_registrarse(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user_email = form.cleaned_data.get('email')
            messages.success(request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            user = authenticate(request, username=username, password=password)
            login(request, user)

            # Aca se crea la instancia de cliente con el primer carrito asociado
            NuevoCliente = Cliente(nombre=first_name, apellido=last_name, dni=0, email=user_email, numero_de_cliente=user.id, usuario=user)
            NuevoCliente.save()
            NuevoCarrito = Carrito(compra_abierta=True, cliente=NuevoCliente, monto_total=0)
            NuevoCarrito.save()
            return redirect('secciones')
    else:
        form = UserRegisterForm()
    return render(request, 'ecommerce/registrarse.html', {'form': form, 'title': 'registrese aquí'})

# Esta vista permite crear mas facil todas las instancias que deben existir en la db inicialmente
def iniciar_db(request):
    # Creacion de categorias
    Categoria1 = Categoria(nombre="Lirio")
    Categoria2 = Categoria(nombre="Frutales")
    Categoria3 = Categoria(nombre="Cactus")
    Categoria4 = Categoria(nombre="Gromineas")
    Categoria5 = Categoria(nombre="Fuentes")
    Categoria6 = Categoria(nombre="Macetas")
    Categoria7 = Categoria(nombre="Herramientas")
    Categoria1.save()
    Categoria2.save()
    Categoria3.save()
    Categoria4.save()
    Categoria5.save()
    Categoria6.save()
    Categoria7.save()
    # Creacion de productos
    Producto1 = Producto(promocion=True, nombre="lirio rojo", descripcion="Simbolismo: Amor y seducción", precio=8500.0, cantidad=20, categoria_id=Categoria1.id)
    Producto2 = Producto(promocion=True, nombre="lirio blanco", descripcion="Simbolismo: Pureza y belleza", precio=8000.0, categoria_id=Categoria1.id)
    Producto3 = Producto(promocion=True, nombre="lirio naranja", descripcion="Simbolismo: Pasion", precio=8000.0, categoria_id=Categoria1.id)
    Producto4 = Producto(promocion=True, nombre="arboles frutales", descripcion="Consultar segun la temporada", precio=8000.0, categoria_id=Categoria2.id)
    Producto5 = Producto(promocion=True, nombre="cactus", descripcion="Fuentes de exito personal y laboral", precio=8000.0, categoria_id=Categoria3.id)
    Producto6 = Producto(promocion=True, nombre="gromineas", descripcion="Plantita espectacular para decorar", precio=8000.0, categoria_id=Categoria4.id)
    Producto7 = Producto(promocion=True, nombre="fuentes", descripcion="Contamos con distintos modelos", precio=8000.0, categoria_id=Categoria5.id)
    Producto8 = Producto(promocion=True, nombre="macetas", descripcion="Variedad de colores y modelos", precio=8000.0, categoria_id=Categoria6.id)
    Producto9 = Producto(promocion=True, nombre="herramientas", descripcion="Palas, regaderas, mangueras y mas", precio=8000.0, categoria_id=Categoria7.id)
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
