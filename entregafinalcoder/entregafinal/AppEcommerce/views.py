from datetime import date
from distutils.debug import DEBUG
from django.shortcuts import render
from AppEcommerce.models import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# a la url que vuelvo
from django.urls import reverse_lazy


def inicio(request):
    return render(request, "index.html")
# Create your views here.


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


def addAuto(request):

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

    return listarAutos(request)


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


# ........................
class AutoUpdate(UpdateView):
    model = Auto
    success_url = reverse_lazy('listarAutos')
    fields = ['nombre', 'precio', 'imagen', 'marca',
              'color', 'modelo', 'anio', 'km']


class AutoCreate(CreateView):
    model = Auto
    success_url = reverse_lazy('listarAutos')
    fields = ['nombre', 'precio', 'imagen' 'marca',
              'color', 'modelo', 'anio', 'km']


class AutoDelete(DeleteView):
    model = Auto
    success_url = reverse_lazy('listarAutos')


class AutoDetalle(DetailView):
    model = Auto
    template_name = "AppEcommerce/auto_detalle.html"
