from rest_framework import serializers
from station.models import Bus, Trip


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ["id", "is_small", "info", "num_seats"]


class TripSerializer(serializers.ModelSerializer):
    bus = BusSerializer()

    class Meta:
        model = Trip
        fields = ["id", "source", "destination", "departure", "bus"]
