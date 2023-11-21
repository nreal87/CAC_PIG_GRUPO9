from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse_lazy
from administracion.models import Categoria, Producto
from administracion.forms import ProductoForm, CategoriaForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

@permission_required('administracion.view_producto', login_url="error_404")
def index_administracion(request):
    #le pasamos que tablas se podan administrar
    context = {"tablas": ['Categoria', 'Producto'],
               "ahora": datetime.now}
    return render(request, "administracion/index_admin.html",context)


#Las vistas para el CRUD de producto lo hacemos con vistas basadas en funciones
@permission_required('administracion.view_producto', login_url="error_404")
def index_producto(request):
    productos = Producto.objects.all()
    context = {'productos' : productos,
               "ahora": datetime.now}
    print(f'{productos}')
    return render(request, "administracion/index_producto.html", context)


@permission_required('administracion.add_producto', login_url="error_404")
def crear_producto(request):
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            #messages.success(request, 'Producto guardado.')
            return redirect('index_producto')

    context = {"form": ProductoForm(),
               "ahora": datetime.now}
    return render(request, "administracion/crear_producto.html", context)

@permission_required('administracion.change_producto', login_url="error_404")
def modificar_producto(request, id_prod):
    
    producto = Producto.objects.get(pk = id_prod)

    if (request.method == 'POST'):
        formulario = ProductoForm(request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_producto')
    else:
        formulario = ProductoForm(instance = producto)

    context = {"form": formulario,
               "ahora": datetime.now}
    return render(request, "administracion/editar_producto.html", {'form': context})


@permission_required('administracion.delete_producto', login_url="error_404")
def eliminar_producto(request, id_prod):
    
    producto = Producto.objects.get(pk = id_prod)
    producto.delete()

    return redirect('index_producto')



#Las vistas para el CRUD de categoria lo hacemos con vistas basadas en clases
class IndexCategoriaView(PermissionRequiredMixin, ListView):
    permission_required = 'administracion.view_categoria'
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'administracion/index_cat.html'


class CrearCategoriaView(PermissionRequiredMixin, CreateView):
    permission_required = 'administracion.add_categoria'
    model = Categoria
    fields = ['nombre']
    template_name = 'administracion/crear_cat.html'
    success_url = reverse_lazy('index_categoria')


class ModificarCategoriaView(PermissionRequiredMixin, UpdateView):
    permission_required = 'administracion.change_categoria'
    model= Categoria
    fields = ['nombre']
    template_name = 'administracion/editar_cat.html'
    success_url = reverse_lazy('index_categoria')


class EliminarCategoriaView(PermissionRequiredMixin, DeleteView):
    permission_required = 'administracion.delete_categoria'
    model= Categoria
    template_name = 'administracion/eliminar_cat.html'
    success_url = reverse_lazy('index_categoria')