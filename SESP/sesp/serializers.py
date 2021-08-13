
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers 


class ExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exit
        fields = ["all"]

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["all"]
        #optional_fields = ['puntos']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["all"]
        

