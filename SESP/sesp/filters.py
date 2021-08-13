import django_filters

from .models import *


class IntermediarioFilter(django_filters.FilterSet):
    class Meta:
        model = Intermediario
        fields = {
            'nombre': ['icontains'],
            'centro': ['exact'],
        }

class PuntoFilter(django_filters.FilterSet):
    class Meta:
        model = PuntoDeAcopio
        fields = {
            'nombre': ['icontains'],
            'centro': ['exact'],
        }