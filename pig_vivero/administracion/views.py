from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse_lazy
from administracion.models import Categoria, Producto
from administracion.forms import ProductoForm, CategoriaForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib import messages

# Create your views here.
def index_administracion(request):
    #le pasamos que tablas se podan administrar
    context = {"tablas": ['Categoria', 'Producto']}
    return render(request, "administracion/index_admin.html",context)

#Las vistas para el CRUD de producto lo hacemos con vistas basadas en funciones
def index_producto(request):
    productos = Producto.objects.all()
    context = {'productos' : productos}
    print(f'{productos}')
    return render(request, "administracion/index_producto.html", context)

def crear_producto(request):
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #messages.success(request, 'Producto guardado.')
            return redirect('index_producto')

    context = {"form": ProductoForm()}
    return render(request, "administracion/crear_producto.html", context)


def modificar_producto(request, id_prod):
    
    producto = Producto.objects.get(pk = id_prod)

    if (request.method == 'POST'):
        formulario = ProductoForm(request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_producto')
    else:
        formulario = ProductoForm(instance = producto)

    return render(request, "administracion/editar_producto.html", {'form': formulario})


def eliminar_producto(request, id_prod):
    
    producto = Producto.objects.get(pk = id_prod)
    producto.delete()

    return redirect('index_producto')



#Las vistas para el CRUD de categoria lo hacemos con vistas basadas en clases
class IndexCategoriaView(ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'administracion/index_cat.html'


class CrearCategoriaView(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'administracion/crear_cat.html'
    success_url = reverse_lazy('index_categoria')


class ModificarCategoriaView(UpdateView):
    model= Categoria
    fields = ['nombre']
    template_name = 'administracion/editar_cat.html'
    success_url = reverse_lazy('index_categoria')


class EliminarCategoriaView(DeleteView):
    model= Categoria    
    template_name = 'administracion/eliminar_cat.html'
    success_url = reverse_lazy('index_categoria')