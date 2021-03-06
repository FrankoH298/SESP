from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Store, Entry, Exit
from .serializers import StoreSerializer, EntrySerializer, ExitSerializer, UserSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from datetime import date, timedelta
from rest_framework.decorators import api_view, permission_classes
import os
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound

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
    queryset = Exit.objects.all()
    serializer_class = ExitSerializer
    permission_classes = [IsStore, permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,SessionAuthentication)

    def get_queryset(self):
        obj = get_object_or_404(Store, user=self.request.user)
        queryset = Exit.objects.filter(store=obj)
        return queryset

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
    


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = IntermediarioFilter
    def get_queryset(self):
    
        obj =  self.request.user
        queryset = User.objects.filter(pk=obj.id)
        return queryset

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsStore])
def total_entries_per_day(request,pk):
    try:
        store = Store.objects.get(pk=pk)
        user = store.user
    except:
        return Response({
            'error': 'Not Found',
        }, status=404)
    if user != request.user:
        return Response({
            "detail": "Authentication credentials were not provided."
        }, status=401)
    store = Store.objects.get(pk=pk)
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

    for entry in entries:
        day = entry.datetime.strftime("%A")
        week[day] += 1

    return Response(week)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsStore])
def total_entries_per_month(request,pk):
    try:
        store = Store.objects.get(pk=pk)
        user = store.user
    except:
        return Response({
            'error': 'Not Found',
        }, status=404)
    if user != request.user:
        return Response({
            "detail": "Authentication credentials were not provided."
        }, status=401)
    store = Store.objects.get(pk=pk)
    entries = Entry.objects.filter(store=store)

    year = {
        'January' : 0,
        'February' : 0,
        'March' : 0,
        'April' : 0,
        'May' : 0,
        'June' : 0,
        'July' : 0,
        'August' : 0,
        'September' : 0,
        'October' : 0,
        'November' : 0,
        'December' : 0,
    }

    for entry in entries:
        month = entry.datetime.strftime('%B')
        year[month] += 1

    return Response(year)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsStore])
def total_entries_last_week(request,pk):
    try:
        store = Store.objects.get(pk=pk)
        user = store.user
    except:
        return Response({
            'error': 'Not Found',
        }, status=404)
    if user != request.user:
        return Response({
            "detail": "Authentication credentials were not provided."
        }, status=401)

    store = Store.objects.get(pk=pk)

    enddate = date.today() + timedelta(days=1)
    startdate = enddate - timedelta(days=7)
    
    entries = Entry.objects.filter(datetime__range=[startdate, enddate], store=store)
    week = {}

    for days in range(0, 7):
        day = (startdate + timedelta(days=days)).strftime("%A %d")
        week[day] = 0

    for entry in entries:
        day = entry.datetime.strftime('%A %d')
        week[day] += 1

    return Response(week)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsStore])
def total_entries_per_hour_last_two_weeks(request,pk):
    try:
        store = Store.objects.get(pk=pk)
        user = store.user
    except:
        return Response({
            'error': 'Not Found',
        }, status=404)
    if user != request.user:
        return Response({
            "detail": "Authentication credentials were not provided."
        }, status=401)

    store = Store.objects.get(pk=pk)

    enddate = date.today() + timedelta(days=1)
    startdate = enddate - timedelta(days=14)
    
    entries = Entry.objects.filter(datetime__range=[startdate, enddate], store=store)

    day = {}

    for hour in range(24):
        day[f'{hour}'] = 0

    for entry in entries:
        hour = entry.datetime.strftime("%-H")
        day[hour] += 1

    return Response(day)


class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()
