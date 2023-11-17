from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index_administracion, name='index_administracion'),
    path('categoria/', views.IndexCategoriaView.as_view(), name="index_categoria"),
    path('categoria/crear/', views.CrearCategoriaView.as_view(), name="crear_categoria"),
    path('categoria/modificar/<int:pk>/', views.ModificarCategoriaView.as_view(), name="modificar_categoria"),
    path('categoria/eliminar/<int:pk>/', views.EliminarCategoriaView.as_view(), name="eliminar_categoria"),

    path('producto/', views.index_producto, name="index_producto"),
    path('producto/crear/', views.crear_producto, name="crear_producto"),
    path('producto/modificar/<int:id_prod>/', views.modificar_producto, name="modificar_producto"),
    path('producto/eliminar/<int:id_prod>/', views.eliminar_producto, name="eliminar_producto"),
    ]