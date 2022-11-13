"""entregafinal URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from AppEcommerce.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    ##path("inicio/", inicio),
    path("addColor/", addColor, name="color_crear"),
    path("addMarca/", addMarca, name="marca_crear"),
    path("", listarAutos, name="listarAutos"),
    path("buscarNombre/", buscarNombre, name="buscarNombre"),
    path("nosotros/", nosotros, name="nosotros"),

    # vistas basadas en clases
    path('auto/editar/<pk>', AutoUpdate.as_view(),
         name='auto_editar'),
    path('auto/crear/', AutoCreate.as_view(),
         name='auto_crear'),
    path('auto/borrar/<pk>', AutoDelete.as_view(),
         name='auto_borrar'),
    path('autoDetalle/<id>', AutoDetalle,
         name='auto_detalle'),

    # login
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='login/login.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),


# rest

    path('api/Autos',AutoViewApiList.as_view(),name="Autos"),
    path('api/Autos/create',AutoViewApiCreate.as_view(),name="AutosCreate"),
    path('api/Autos/Detail/<pk>/',AutoRetrieveApiView.as_view(),name="AutoDetail"),
    path('api/Autos/Delete/<pk>/',AutoDeleteApiView.as_view(),name="AutoDelete"),
    path('api/Autos/Update/<pk>/',AutoUpdateApiView.as_view(),name="AutoUpdate")





]
