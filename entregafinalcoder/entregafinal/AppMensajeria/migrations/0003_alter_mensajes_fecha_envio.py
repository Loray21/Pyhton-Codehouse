# Generated by Django 4.1 on 2022-09-29 23:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMensajeria', '0002_alter_mensajes_fecha_envio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='fecha_envio',
            field=models.DateField(default=datetime.datetime(2022, 9, 29, 20, 36, 7, 752336)),
        ),
    ]
