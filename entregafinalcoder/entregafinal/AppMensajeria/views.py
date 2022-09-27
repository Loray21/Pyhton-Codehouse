
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


def crearMensaje(request, id):
    if (request.method == "POST"):
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            message = mensajes(
                message=form.cleaned_data['mensaje'], user_id=request.user.id, fecha_envio=form.cleaned_data['fecha_envio'])
            message.save()
            reverse_lazy('auto_detalle')
        else:
            reverse_lazy('auto_detalle', {
                         "mensaje": 'No se pudo enviar el mensaje'})
    else:
        form = CreateMessageForm
        reverse_lazy('auto_detalle', {
            "form": form})


class MensajeUpdate(UpdateView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass


class MensajeDelete(DeleteView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass
# Create your views here.
