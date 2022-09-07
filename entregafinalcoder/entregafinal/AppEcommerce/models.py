from django.db import models


class Marca(models.Model):
    marca = models.CharField(max_length=50)


class Color(models.Model):
    color = models.CharField(max_length=50)


class Auto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='autos/', null=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    km = models.FloatField()


# Create your models here.
