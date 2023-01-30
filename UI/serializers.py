# This is our serializer page
from rest_framework import serializers
from UI.models import System

class SystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = System
        fields = ('id', 'url', 'name', 'language', 'price')