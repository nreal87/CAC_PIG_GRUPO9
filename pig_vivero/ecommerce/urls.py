"""pig_vivero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.secciones, name="secciones"),
    path('productos/', views.productos, name="productos"),
    #ruta parametrizada, ingresamos a cada categoria de productos
    path('productos/<int:id_prod>/', views.producto_id, name="producto_id"),
    path('productos/<str:categoria>/', views.producto_categoria, name="productos_categoria"),
    # path('ver_carrito/', views.CarritoListView.as_view(), name="ver_carrito"), 
    path('ver_carrito/', views.ver_carrito, name="ver_carrito"), 
    path('comprar_carrito/',views.comprar_carrito, name="comprar_carrito"),
    path('login/', views.ecommerce_login, name="ecommerce_login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='ecommerce/index.html'),name="ecommerce_logout"),
    path('registrarse/',views.ecommerce_registrarse, name="ecommerce_registrarse"),
    path('error/', views.error, name="error_404"),
    # Esta vista se crea para inicializar la db con instancias de los modelos mas facilmente
    # path('iniciar_db/', views.iniciar_db, name="iniciar_db"),
    # Esta url debe ser la ultima porque si no matcheo con otra antes es porque va a asumir que es una seccion del index
    path('<str:seccion>/',views.secciones, name="secciones"),
]
