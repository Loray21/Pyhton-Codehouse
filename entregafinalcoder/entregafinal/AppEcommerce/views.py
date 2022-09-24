from datetime import date
from distutils.debug import DEBUG
from operator import is_not
from django.shortcuts import render
from AppEcommerce.models import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# a la url que vuelvo
from django.urls import reverse_lazy
from AppEcommerce.forms import UserRegisterForm, UserEditForm


def inicio(request):
    return render(request, "index.html")
# Create your views here.


def nosotros(request):
    return render(request, "nosotros/nosotros.html")


def render_form(request):
    return render(request, "formAuto.html")


def render_marca(request):
    return render(request, "formMarca.html")


def render_color(request):
    return render(request, "formColor.html")


def addColor(request):
    if request.method == "POST":
        color_auto = request.POST.get("color")
        color = Color(color=color_auto)
        color.save()

    return listarAutos(request)


def addMarca(request):
    if request.method == "POST":
        marca_auto = request.POST.get("marca")
        marca = Marca(marca=marca_auto)
        marca.save()

    return listarAutos(request)


"""def addAuto(request):

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        imagen = request.FILES.get("imagen")
        marca = request.POST.get("marca")
        color = request.POST.get("color")
        modelo = request.POST.get("modelo")
        anio = request.POST.get("anio")
        km = request.POST.get("km")
        auto = Auto(nombre=nombre, precio=precio,
                    imagen=imagen, marca=marca, color=color, modelo=modelo, anio=anio,
                    km=km)
        auto.save()

    return listarAutos(request)"""


def listarAutos(request):
    # traeme de la base, TODOS los cursos que tengan esa comision
    autos = Auto.objects.all()
    return render(request, "index.html", {"autos": autos})


def buscarNombre(request):

    if request.GET["nombre"]:
        nombre_auto = request.GET["nombre"]
        autos = Auto.objects.filter(nombre=nombre_auto)
        return render(request, "index.html", {"autos": autos})

    else:
        return listarAutos(request)
# .......................


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = request.POST["username"]
            clave = request.POST["password"]
            # se fija que exista el usuario sino no devuelve nada
            usuario = authenticate(username=user, password=clave)
            if usuario is not None:
                login(request, usuario)
                return listarAutos(request)
            else:
                return render(request, "login/login.html", {"formulario": form, 'mensaje': f'Usuario o contraseña incorrecto'})
        else:
            return render(request, "login/login.html", {"formulario": form, 'mensaje': f'Usuario o contraseña incorrecto'})

    else:
        form = AuthenticationForm()
        return render(request, "login/login.html", {"formulario": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # me traigo el username limpito
            username = form.cleaned_data.get('username')
            # guardo la data del user en la bbdd
            form.save()
            return render(request, "login/login.html", {"mensaje": f"el usuario {username} se creo correctamente"})
        else:
            return render(request, "register/register.html", {"formulario": form, "mensaje": "DATOS INVALIDOS"})
    else:
        form = UserRegisterForm()
        return render(request, "register/register.html", {"formulario": form})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, "index.html", {"mensaje": "Perfil editado correctamente"})
        else:
            return render(request, "editarPerfil.html", {"formulario": form, "usuario": usuario, "mensaje": "FORMULARIO INVALIDO"})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "editar_perfil.html", {"formulario": form, "usuario": usuario})


# ........................


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    success_url = reverse_lazy('listarAutos')
    fields = ['nombre', 'precio', 'imagen', 'marca',
              'color', 'modelo', 'anio', 'km']


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    success_url = reverse_lazy('listarAutos')
    fields = ['nombre', 'precio', 'imagen', 'marca',
              'color', 'modelo', 'anio', 'km']


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = reverse_lazy('listarAutos')


class AutoDetalle(DetailView):
    model = Auto
    template_name = "AppEcommerce/auto_detalle.html"
