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
from AppEcommerce.forms import *

# a la url que vuelvo
from django.urls import reverse_lazy
from AppEcommerce.forms import UserRegisterForm, UserEditForm
# from AppMensajeria.views import crearMensaje
# from AppMensajeria.views import listarMensajes


# Create your views here.


def nosotros(request):
    return render(request, "nosotros/nosotros.html", {"avatar": obtenerAvatar(request)})


def addColor(request):
    if request.method == "POST":
        form = colorForm(request.POST)
        if (form.is_valid):
            color_auto = request.POST.get("color")
            color = Color(color=color_auto)
            color.save()
        return listarAutos(request)
    else:
        form = colorForm
        return render(request, "color.html", {"avatar": obtenerAvatar(request), "form": form})


def addMarca(request):
    if request.method == "POST":
        form = marcaForm(request.POST)
        if (form.is_valid):
            marca_auto = request.POST.get("marca")
            marca = Marca(marca=marca_auto)
            marca.save()
        return listarAutos(request)
    else:
        form = marcaForm
        return render(request, "marca.html", {"avatar": obtenerAvatar(request), "form": form})


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
    return render(request, "index.html", {"autos": autos, "avatar": obtenerAvatar(request)})


def buscarNombre(request):

    if request.GET["nombre"]:
        nombre_auto = request.GET["nombre"]
        autos = Auto.objects.filter(nombre=nombre_auto)
        if len(autos) > 0:
            return render(request, "index.html", {"autos": autos})
        else:
            return render(request, "home/notfound.html", {"avatar": obtenerAvatar(request)})

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
            return render(request, "login/login.html", {"mensaje": f"Su usuario {username} se creo correctamente, Ingrese"})
        else:
            return render(request, "register/register.html", {"formulario": form})
    else:
        form = UserRegisterForm()
        return render(request, "register/register.html", {"formulario": form})


@ login_required
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
            return render(request, "perfil/editar_perfil.html", {"mensaje": "Perfil editado correctamente", "formulario": form, })
        else:
            return render(request, "perfil/editar_perfil.html", {"formulario": form, "usuario": usuario, "mensaje": "FORMULARIO INVALIDO", "avatar": obtenerAvatar(request)})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "perfil/editar_perfil.html", {"formulario": form, "usuario": usuario, "avatar": obtenerAvatar(request)})


def AutoDetalle(request, id):
    auto = Auto.objects.get(id=id)
    print(str(auto))
    return render(request, "AppEcommerce/auto_detalle.html", {"auto": auto, "avatar": obtenerAvatar(request)})


@ login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = avatarForm(request.POST, request.FILES)
        if (form.is_valid()):
            avatarViejo = avatar.objects.filter(user=request.user)
            if (len(avatarViejo) > 0):
                avatarViejo[0].delete()
            avat = avatar(imagen=form.cleaned_data['imagen'], user=request.user,
                          )

            avat.save()
        return render(request, "perfil/agregar_avatar.html", {"avatarForm": form, "mensaje": "avatar editado correctamente", "avatar": obtenerAvatar(request)})
    else:
        Form = avatarForm()
        return render(request, "perfil/agregar_avatar.html", {"avatarForm": Form, "avatar": obtenerAvatar(request)})
        # ........................


@ login_required
def obtenerAvatar(request):
    avat = avatar.objects.filter(user=request.user)
    if (len(avat) != 0):
        print(avat[0].imagen.url)

        return (avat[0].imagen.url)
    else:
        return "https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/fox.jpg"


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['avatar'] = obtenerAvatar(self.request)
        context['accion'] = "Editar Auto"
        return context
    success_url = reverse_lazy('listarAutos')

    fields = ['nombre', 'precio', 'imagen', 'marca',
              'color', 'modelo', 'anio', 'km']


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    success_url = reverse_lazy('listarAutos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['avatar'] = obtenerAvatar(self.request)
        context['accion'] = "Agregar Auto"
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    fields = ['nombre', 'precio', 'imagen', 'marca',
              'color', 'modelo', 'anio', 'km', 'descripcion']


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto

    success_url = reverse_lazy('listarAutos')
