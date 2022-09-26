from email import message
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from AppEcommerce.models import *


class CreateMessageForm():
    message = forms.CharField()
    fields = ['message', 'user_id', 'fecha_envio']
