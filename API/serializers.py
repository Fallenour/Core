from rest_framework import serializers
from UI.models import Event, System

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('__all__')

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ('__all__')