from rest_framework import serializers
from station.models import Bus, Trip, Facility


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "name"]


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ["id", "is_small", "info", "num_seats", "facilities"]


class BusListSerializer(BusSerializer):
    facilities = FacilitySerializer(many=True)


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ["id", "source", "destination", "departure", "bus"]


class TripListSerializer(TripSerializer):
    bus = BusSerializer()
