from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Store, Entry, Exit
from .serializers import StoreSerializer, EntrySerializer, ExitSerializer
from django.shortcuts import render, get_object_or_404
#rest framework imports
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
import datetime
from rest_framework.decorators import api_view, permission_classes

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
    permission_classes = [IsStore, permissions.IsAuthenticated]
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

    def create(self, request, *args, **kwargs):
        store = Store.objects.get(user=request.user)
        request.data['store'] = store.pk
        
        if store.actual_people == 0:
            return Response(
                {
                    'success': 'el local esta vacio',
                    'personas_actuales': store.actual_people,
                    'capacidad_maxima': store.max_people
                },
                status=203
            )
        super().create(request, *args, **kwargs)
        return Response(
            {
                'success': 'nuevo egresante agregado',      
                'personas_actuales': store.actual_people-1,
                'capacidad_maxima': store.max_people
            },
            status=200
        )
        
        
    

    
    def log(self, request, *args, **kwargs):
        full_log = Exit.objects.all()
        serializer = ExitSerializer(full_log, many=True)

        return Response(serializer.data)


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsStore, permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = IntermediarioFilter
    def get_queryset(self):

        obj = get_object_or_404(Store, user=self.request.user)
        queryset = Entry.objects.filter(store=obj)
        return queryset
    
    def create(self, request, *args, **kwargs):
        store = Store.objects.get(user=self.request.user)
        if store.is_full:
            return Response(
                {
                    'success': 'el local esta lleno',
                    'personas_actuales': store.actual_people,
                    'capacidad_maxima': store.max_people
                }, 
                status=203
            )
        request.data['store'] = store.pk
        super().create(request, *args, **kwargs)
        return Response(
            {
                'success': 'nuevo ingresante agregado',
                'personas_actuales': store.actual_people+1,
                'capacidad_maxima': store.max_people
            }, 
            status=200
        )
                         
    

    def log(self, request, *args, **kwargs):
        full_log = Entry.objects.all()
        serializer = EntrySerializer(full_log, many=True)

        return Response(serializer.data)


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsStore]
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = IntermediarioFilter
    

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsStore])
def total_entries_by_day(request):

    store = Store.objects.get(user=request.user)
    entries = Entry.objects.filter(store=store)

    week = {
        'Monday' : 0,
        'Tuesday' : 0,
        'Wednesday' : 0,
        'Thursday' : 0,
        'Friday' : 0,
        'Saturday' : 0,
        'Sunday' : 0,
    }

    for x in entries:
        day = x.datetime.strftime("%A")
        week[day] += 1

    return Response(week)


