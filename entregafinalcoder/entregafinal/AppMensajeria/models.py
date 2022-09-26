
import datetime
from time import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class mensajes(models.Model):
    mensaje = models.CharField(max_length=120)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_envio = models.DateField(default=datetime.datetime.now())
