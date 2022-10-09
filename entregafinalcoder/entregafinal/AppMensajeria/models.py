
import datetime
from unittest.util import _MAX_LENGTH
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class mensajes_chat(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    mensaje = models.CharField(max_length=120)
    fecha_envio = models.DateField(default=timezone.now)


class chat(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='send')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receive')
    mensaje = models.CharField(max_length=120)
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.mensaje
