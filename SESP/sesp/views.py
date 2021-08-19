from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
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
        
from rest_framework.response import Response
from rest_framework.decorators import action, authentication_classes, permission_classes

# Create your views here.
def actual_view(request, store):
    user = User.objects.get(username=store)
    store = get_object_or_404(Store, user=user)
    return render(request, "actual.html", {"store": store})

def stats_view(request, store):
    user = User.objects.get(username=store)
    store = get_object_or_404(Store, user=user)
    return render(request, "stats.html", {"store": store})


class ExitViewSet(viewsets.ModelViewSet):
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
    
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        store = Store.objects.get(user=self.request.user)
        request.data['store'] = store.pk
        super().create(request, *args, **kwargs)
        if store.actual_people == 0:
            response = Response({'success': 'nuevo egresante agregado exitosamente',
                             'warning': 'hubo uno o varios ingresos no notificados',
                                 'personas_actuales': store.actual_people,
                                 'capacidad_maxima': store.max_people
                                 }, status=201)
        else:
            response = Response({'success': 'nuevo egresante agregado exitosamente',
                                 'personas_actuales': store.actual_people,
                                 'capacidad_maxima': store.max_people
                                 }, status=201)
        return response
    

    @action(detail=False, permission_classes=[permissions.IsAdminUser])
    def log(self, request, *args, **kwargs):
        full_log = Exit.objects.all()
        serializer = ExitSerializer(full_log, many=True)

        return Response(serializer.data)


    def get_queryset(self):
        store = Store.objects.get(user=self.request.user)
        shop_log = Exit.objects.filter(store=store)

        return shop_log


class EntryViewSet(viewsets.ModelViewSet):
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
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        store = Store.objects.get(user=self.request.user)
        if store.is_full:
            return Response({'error': 'el local esta lleno',
                             'personas_actuales': store.actual_people,
                             'capacidad_maxima': store.max_people}, status=500)
        request.data['store'] = store.pk
        super().create(request, *args, **kwargs)
        return Response({'success': 'nuevo ingresante agregado exitosamente',
                         'personas_actuales': store.actual_people,
                         'capacidad_maxima': store.max_people
                         }, status=201)
    

    @action(detail=False, permission_classes=[permissions.IsAdminUser])
    def log(self, request, *args, **kwargs):
        full_log = Entry.objects.all()
        serializer = EntrySerializer(full_log, many=True)

        return Response(serializer.data)


    def get_queryset(self):
        store = Store.objects.get(user=self.request.user)
        shop_log = Entry.objects.filter(store=store)

        return shop_log


class StoreViewSet(viewsets.ModelViewSet):
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
    http_method_names = ['get'] # metodos http permitidos
