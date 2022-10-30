from dataclasses import field
from rest_framework import serializers

from AppEcommerce.models import Auto

class AutoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Auto
        fields = [
                'user',
                'nombre',
                'precio',
                'imagen',
                'marca',
                'color',
                'modelo',
                'anio',
                'km']


