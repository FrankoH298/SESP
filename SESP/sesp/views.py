from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Store, Entry, Exit
from .serializers import StoreSerializer, EntrySerializer, ExitSerializer
#rest framework imports
from rest_framework import permissions, viewsets
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