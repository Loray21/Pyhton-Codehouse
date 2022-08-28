from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField(auto_now_add=True, blank=True)
