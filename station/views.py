from rest_framework import mixins, viewsets

from station.models import Bus
from station.serializers import BusSerializer


class BusViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
