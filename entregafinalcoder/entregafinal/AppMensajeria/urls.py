from django.contrib import admin
from django.urls import path, include
from AppMensajeria.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    # vistas basadas en clases
    path('mensaje/editar/<pk>', MensajeUpdate.as_view(),
         name='mensaje_editar'),
    path('mensaje/crear/<int:sender>/<int:receiver>/', crearMensaje,
         name='mensaje_crear'),
    path('mensaje/borrar/<pk>', MensajeDelete.as_view(),
         name='mensaje_borrar'),
    path('chat/<int:sender>/<int:receiver>/',
         message_view, name='render_mensajes')


]

"""path('rendermensajes/<user>', rendermensajes,
         name='render_mensajes'),"""
