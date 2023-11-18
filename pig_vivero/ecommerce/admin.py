from django.contrib import admin
from administracion.models import Categoria, Producto, ItemCarrito, Carrito
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(ItemCarrito)
admin.site.register(Carrito)