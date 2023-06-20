from rest_framework import generics

from UI.models import System, Event
from .serializers import EventSerializer, SystemSerializer


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        system = self.request.query_params.get('system')
        if system is not None:
            queryset = queryset.filter(system=system)
        return queryset

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class SystemList(generics.ListCreateAPIView):
    serializer_class = SystemSerializer
    queryset = System.objects.all()

class SystemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SystemSerializer
    queryset = System.objects.all()


# Source: https://www.youtube.com/watch?v=OJdFj5hPAKs