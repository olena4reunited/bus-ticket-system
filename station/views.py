from rest_framework import viewsets

from station.models import Bus, Trip
from station.serializers import BusSerializer, TripSerializer, TripListSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class TripViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return TripListSerializer

        return TripSerializer

    def get_queryset(self):
        queryset = Trip.objects.all()
        if self.action == "list":
            return queryset.select_related()
        return queryset
