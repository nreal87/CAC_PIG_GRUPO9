from django.contrib import admin

from administracion.models import Cliente, Categoria, Producto, Carrito, ItemCarrito
from django.contrib.auth.models import User

# Register your models here.

#con esto registramos los modelos que tiene la relacion muchos a muchos
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(ItemCarrito)
admin.site.register(Carrito)