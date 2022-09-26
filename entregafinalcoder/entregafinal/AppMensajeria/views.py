
from django.shortcuts import render
from AppMensajeria.models import *
from django.views.generic import *
from django.urls import reverse_lazy
from AppMensajeria.forms import CreateMessageForm


class MensajeCreate(CreateView):
    model = mensajes
    form_class = CreateMessageForm
    success_url = reverse_lazy('auto_detalle')


class MensajeUpdate(UpdateView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass


class MensajeDelete(DeleteView):
    model = mensajes
    success_url = reverse_lazy('auto_detalle')
    pass
# Create your views here.
