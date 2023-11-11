from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('crear_producto/', views.crear_producto, name="crear_producto"),
    ]