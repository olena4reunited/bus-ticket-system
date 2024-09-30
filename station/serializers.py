from rest_framework import serializers
from station.models import Bus


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ["id", "is_small", "info", "num_seats"]
