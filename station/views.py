from rest_framework import viewsets

from station.models import Bus, Trip
from station.serializers import BusSerializer, TripSerializer, TripListSerializer, BusListSerializer


class BusViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return BusListSerializer

        return BusSerializer

    def get_queryset(self):
        queryset = Bus.objects.all()
        if self.action == "list":
            return queryset.prefetch_related("facilities")
        return queryset



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
