from rest_framework import generics

from station.models import Bus
from station.serializers import BusSerializer


class BusList(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
