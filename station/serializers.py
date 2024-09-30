from rest_framework import serializers
from station.models import Bus


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ["id", "info", "num_seats"]
        read_only_fields = ["id"]
