
from django.shortcuts import render, redirect
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


def listarMensajes(sender, receiver):
    messages = mensajes.objects.filter(sender=sender, receiver=receiver) | mensajes.objects.filter(
        sender_id=receiver, receiver_id=sender)
    return messages


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('auto_detalle')
    if request.method == "GET":
        return render(request, 'appMensajeria/rendermensajes.html',
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': mensajes.objects.filter(sender_id=sender, receiver_id=receiver) |
                       mensajes.objects.filter(sender_id=receiver, receiver_id=sender)})


def crearMensaje(request, sender, receiver):
    userSender = User.objects.get(id=sender)
    userReceiver = User.objects.get(id=receiver)
    if (request.method == "POST"):
        message = mensajes(
            mensaje=request.POST.get("mensaje"), sender=userSender, receiver=userReceiver, fecha_envio=datetime.datetime.now())
        message.save()

        return render(request, 'appMensajeria/rendermensajes.html', {"mensajes": listarMensajes(userSender, userReceiver), "receiver": userReceiver, "sender": userSender})
    else:
        return render(request, 'appMensajeria/rendermensajes.html', {"mensaje": 'No se pudo enviar el mensaje'})


"""def rendermensajes(request, user):
    return render(request, 'appMensajeria/rendermensajes.html', {"user": user, "mensajes": listarMensajes(request.user, user)})"""


class MensajeUpdate(UpdateView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass


class MensajeDelete(DeleteView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass
# Create your views here.
