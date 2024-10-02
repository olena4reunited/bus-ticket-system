from django.db.models import Count, F
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
    @staticmethod
    def _params_to_ints(query_string):
        """
        Converts a query string into a list of integers.
        """
        return [int(str_id) for str_id in query_string.split(",")]

    def get_serializer_class(self):
        if self.action == "list":
            return BusListSerializer
        elif self.action == "retrieve":
            return BusRetrieveSerializer

        return BusSerializer

    def get_queryset(self):
        queryset = Bus.objects.all()

        facilities = self.request.query_params.get("facilities", None)

        if facilities:
            facilities = self._params_to_ints(facilities)
            queryset = queryset.filter(facilities__id__in=facilities)

        if self.action == ["list", "retrieve"]:
            return queryset.prefetch_related("facilities")

        return queryset.distinct()


class TripViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return TripListSerializer
        elif self.action == "retrieve":
            return TripRetrieveSerializer

        return TripSerializer

    def get_queryset(self):
        queryset = Trip.objects.all()

        if self.action == "list":
            queryset = (
                queryset
                .select_related()
                .annotate(tickets_available=F("bus__num_seats") - Count("tickets"))
            )
        elif self.action == "retrieve":
            return queryset.select_related()

        return queryset.order_by("id")


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
