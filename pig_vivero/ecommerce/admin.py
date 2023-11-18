from django.contrib import admin
from administracion.models import Categoria, Producto
from django.contrib.auth.models import User
# Register your models here.

#con esto registramos los modelos que tiene la relacion muchos a muchos
class ViveroAdminSite(admin.AdminSite):
    site_header = "Administracion Vivero Los Lirios."
    site_title = "Administracion Los Lirios"
    index_title = "Administracion"
    

vivero_admin = ViveroAdminSite(name = "viveroAdmin")
vivero_admin.register(User)
vivero_admin.register(Categoria)
vivero_admin.register(Producto)
