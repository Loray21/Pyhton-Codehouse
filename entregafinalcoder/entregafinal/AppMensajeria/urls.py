from django.contrib import admin
from django.urls import path, include
from AppMensajeria.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    # vistas basadas en clases
    path('mensaje/editar/<pk>', MensajeUpdate.as_view(),
         name='mensaje_editar'),
    path('mensaje/crear/', MensajeCreate.as_view(),
         name='mensaje_crear'),
    path('mensaje/borrar/<pk>', MensajeDelete.as_view(),
         name='mensaje_borrar')



]
