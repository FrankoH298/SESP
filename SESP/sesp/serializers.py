
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers 


class ExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exit
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):

    actual_people = serializers.ReadOnlyField()
    is_full = serializers.ReadOnlyField()

    class Meta:
        model = Store
        fields = '__all__'