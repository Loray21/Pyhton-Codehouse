from django.db import models
from django.contrib.auth.models import User


class Marca(models.Model):
    marca = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.marca


class Color(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.color


class Auto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='autos/', null=True)
    marca = models.ForeignKey(
        Marca, verbose_name="Marca", on_delete=models.CASCADE)
    color = models.ForeignKey(
        Color, verbose_name="color", on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    km = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre + " " + self.modelo + " " + str(self.anio)


class avatar(models.Model):
    imagen = models.ImageField(upload_to='avatar/', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Create your models here.
