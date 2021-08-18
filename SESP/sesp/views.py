from django.shortcuts import render
from .models import Store, Entry, Exit
from .serializers import StoreSerializer, EntrySerializer, ExitSerializer
from django.shortcuts import render, get_object_or_404
#rest framework imports
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.
class IsStore(permissions.BasePermission):
    """
    Custom permission to only allow Stores make certain actions.
    """
    
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # Write permissions are only allowed to the owner of the snippet.
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True

        else:
            
            try:
                
                obj = Store.objects.get(user=request.user)
                return True
            except:
                print("User has no store")
                return False
            
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
                # Check permissions for read-only request
            return True

        else:
            
            try:
                
                centro = Store.objects.get(user=request.user)
                try :
                    centro_obj = obj.centro
                except:
                    centro_obj = obj
                if centro_obj == centro:
                    return True
                else:
                    return False
            except:
                return False
        
class ExitViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Exits.
    """
    queryset = Exit.objects.all()
    serializer_class = ExitSerializer
    permission_classes = [IsStore]
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = PuntoFilter
    def get_queryset(self):
        obj = get_object_or_404(Store, user=self.request.user)
        queryset = Exit.objects.filter(store=obj)
        return queryset
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
    permission_classes = [IsStore]
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = IntermediarioFilter
    def get_queryset(self):
        obj = get_object_or_404(Store, user=self.request.user)
        queryset = Entry.objects.filter(store=obj)
        return queryset
    """def perform_create(self, serializer):
        obj = get_object_or_404(Store, user=self.request.user)
        
        serializer.save(store=obj)"""

class StoreViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for entrys.

    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsStore]
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = IntermediarioFilter
    
    """def perform_create(self, serializer):
        centro = get_object_or_404(CentroDeReciclaje, usuario=self.request.user)
        puntos = centro.puntos.all()
        serializer.save(centro=centro,puntos=puntos)"""