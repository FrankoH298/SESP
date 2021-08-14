from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Store, Entry, Exit
from .serializers import StoreSerializer, EntrySerializer, ExitSerializer
#rest framework imports
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, authentication_classes, permission_classes

# Create your views here.
class ExitViewSet(viewsets.ModelViewSet):
    queryset = Exit.objects.all()
    serializer_class = ExitSerializer
    permission_classes = [permissions.IsAuthenticated]
    

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