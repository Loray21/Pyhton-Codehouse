
from django.shortcuts import render
from AppMensajeria.models import *
from django.views.generic import *
from django.urls import reverse_lazy

from AppMensajeria.forms import CreateMessageForm
from AppMensajeria.models import mensajes
from AppEcommerce.models import Auto
from django.contrib.auth.models import User


class MensajeCreate(CreateView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    fields = ['mensaje', 'fecha_envio']


def listarMensajes(sender):
    messages = mensajes.objects.filter(sender=sender)
    return messages


def crearMensaje(request, user):
    userSender = request.user
    userReceiver = User.objects.get(username=user)
    if (request.method == "POST"):
        message = mensajes(
            mensaje=request.POST.get("mensaje"), sender=userSender, receiver=userReceiver, fecha_envio=datetime.datetime.now())
        message.save()

        return rendermensajes(request, request.user)
    else:
        return render(request, 'appMensajeria/rendermensajes.html', {"mensaje": 'No se pudo enviar el mensaje'})


def rendermensajes(request, user):
    return render(request, 'appMensajeria/rendermensajes.html', {"user": user, "mensajes": listarMensajes(request.user)})


class MensajeUpdate(UpdateView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass


class MensajeDelete(DeleteView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass
# Create your views here.
