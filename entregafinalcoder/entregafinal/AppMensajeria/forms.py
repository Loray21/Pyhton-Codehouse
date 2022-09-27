from email import message
from django.forms import ModelForm
from django import forms
from AppEcommerce.models import *


class CreateMessageForm(forms.Form):
    message = forms.CharField()
    fecha_envio = forms.DateField()
    ##fields = ['message', 'fecha_envio']
