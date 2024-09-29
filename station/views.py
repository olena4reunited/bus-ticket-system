from rest_framework import generics, mixins, viewsets

from station.models import Bus
from station.serializers import BusSerializer


class BusList(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer



class BusDetail(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
