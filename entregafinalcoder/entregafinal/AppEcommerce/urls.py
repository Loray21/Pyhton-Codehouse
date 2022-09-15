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
urlpatterns = [
    ##path("inicio/", inicio),
    path("FormAuto/", render_form),
    path("FormColor/", render_color),
    path("FormMarca/", render_marca),
    path("addAuto/", addAuto, name="addAuto"),
    path("addColor/", addColor, name="addColor"),
    path("addMarca/", addMarca, name="addMarca"),
    path("", listarAutos, name="listarAutos"),
    path("buscarNombre/", buscarNombre, name="buscarNombre"),

    # vistas basadas en clases
    path('auto/editar/<pk>', AutoUpdate.as_view(),
         name='auto_editar'),
    path('auto/crear/', AutoCreate.as_view(),
         name='auto_crear'),
    path('auto/borrar/<pk>', AutoDelete.as_view(),
         name='auto_borrar'),
    path('autoDetalle/<pk>', AutoDetalle.as_view(),
         name='auto_detalle'),



]
