from django.shortcuts import render
from datetime import datetime
from administracion.forms import ProductoForm
from administracion.models import Categoria
from django.views.generic import ListView
from django.contrib import messages

# Create your views here.
#Las vistas para el CRUD de producto lo hacemos con vistas basadas en funciones
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

#Las vistas para el CRUD de categoria lo hacemos con vistas basadas en clases
class CrearCategoriaView(ListView):

    model= Categoria
    field = ['nombre']
    template = 'crear_producto.html'
