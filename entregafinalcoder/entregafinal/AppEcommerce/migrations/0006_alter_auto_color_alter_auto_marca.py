# Generated by Django 4.1 on 2022-09-25 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppEcommerce', '0005_alter_auto_color_alter_auto_imagen_alter_auto_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEcommerce.color', verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEcommerce.marca', verbose_name='Marca'),
        ),
    ]
