from email import message
from django.forms import ModelForm
from django import forms
from AppEcommerce.models import *


class CreateMessageForm(forms.Form):
    message = forms.CharField()
    users = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select)

    # fields = ['message', 'fecha_envio']
