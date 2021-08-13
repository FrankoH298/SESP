from django.shortcuts import render
from .models import Store, Entry, Exit
from .serializers import StoreSerializer, EntrySerializer, ExitSerializer
#rest framework imports
from rest_framework import permissions, viewsets

# Create your views here.
class ExitViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Exits.
    """
    queryset = Exit.objects.all()
    serializer_class = ExitSerializer
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = PuntoFilter

    """def perform_create(self, serializer):
        centro = get_object_or_404(CentroDeReciclaje, usuario=self.request.user)
        serializer.save(centro=centro)"""
    
    

class EntryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for entrys.

    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [True]
    #authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = IntermediarioFilter
    
    """def perform_create(self, serializer):
        centro = get_object_or_404(CentroDeReciclaje, usuario=self.request.user)
        puntos = centro.puntos.all()
        serializer.save(centro=centro,puntos=puntos)"""

class StoreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for entrys.

    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [True]
    #authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = IntermediarioFilter
    
    """def perform_create(self, serializer):
        centro = get_object_or_404(CentroDeReciclaje, usuario=self.request.user)
        puntos = centro.puntos.all()
        serializer.save(centro=centro,puntos=puntos)"""