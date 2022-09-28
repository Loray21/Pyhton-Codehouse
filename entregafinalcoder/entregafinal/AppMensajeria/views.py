
from django.shortcuts import render
from AppMensajeria.models import *
from django.views.generic import *
from django.urls import reverse_lazy

from AppMensajeria.forms import CreateMessageForm
from AppMensajeria.models import mensajes


class MensajeCreate(CreateView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    fields = ['mensaje', 'fecha_envio']


def crearMensaje(request):
    user = request.user
    if (request.method == "POST"):
        message = mensajes(
            mensaje=request.POST.get("mensaje"), user_id=user, fecha_envio=datetime.datetime.now())
        message.save()
        return (request, 'auto_detalle.html', {"usuario": user})
    else:
        return render(request, 'auto_detalle.html', {"mensaje": 'No se pudo enviar el mensaje'})


class MensajeUpdate(UpdateView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass


class MensajeDelete(DeleteView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass
# Create your views here.
