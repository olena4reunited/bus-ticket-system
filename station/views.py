from rest_framework import viewsets

from station.models import (
    Bus,
    Trip,
    Facility, Order
)
from station.serializers import (
    BusSerializer,
    TripSerializer,
    TripListSerializer,
    BusListSerializer,
    FacilitySerializer,
    BusRetrieveSerializer,
    TripRetrieveSerializer, OrderSerializer
)


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class BusViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return BusListSerializer
        elif self.action == "retrieve":
            return BusRetrieveSerializer

        return BusSerializer

    def get_queryset(self):
        queryset = Bus.objects.all()
        if self.action == ["list", "retrieve"]:
            return queryset.prefetch_related("facilities")
        return queryset


class TripViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return TripListSerializer
        elif self.action == "retrieve":
            return TripRetrieveSerializer

        return TripSerializer

    def get_queryset(self):
        queryset = Trip.objects.all()
        if self.action == ["list", "retrieve"]:
            return queryset.select_related()
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
