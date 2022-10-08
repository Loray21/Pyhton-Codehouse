from tkinter import Widget
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from AppEcommerce.models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="username")
    email = forms.EmailField(label="email")
    password1 = forms.CharField(
        # los widget son onjs que tienen representacion en el navegadro
        label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        # los widget son onjs que tienen representacion en el navegadro
        label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # saca los mensjae de ayuda
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label='Modificar Nombre')
    last_name = forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k: "" for k in fields}


class autoForm(forms.Form):
    class Meta:
        model = Auto
        fields = [
            'nombre',
            'precio',
            'imagen',
            'marca',
            'color',
            'modelo',
            'anio',
            'km']


class avatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")
