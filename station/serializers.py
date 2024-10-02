from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from station.models import Bus, Trip, Facility, Ticket, Order


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "name"]


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ["id", "is_small", "info", "num_seats", "facilities"]


class BusListSerializer(BusSerializer):
    facilities = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


class BusRetrieveSerializer(BusSerializer):
    facilities = FacilitySerializer(many=True)


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ["id", "source", "destination", "departure", "bus"]


class TripListSerializer(TripSerializer):
    bus_info = serializers.CharField(
        source="bus.info", read_only=True
    )
    bus_num_seats = serializers.IntegerField(
        source="bus.num_seats", read_only=True
    )

    class Meta:
        model = Trip
        fields = ["id", "source", "destination", "departure", "bus_info", "bus_num_seats"]


class TripRetrieveSerializer(TripSerializer):
    bus = BusRetrieveSerializer(many=False, read_only=True)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "seat", "trip"]
        validators = [
            UniqueTogetherValidator(
                queryset=Ticket.objects.all(),
                fields=["seat", "trip"]
            )
        ]

    def validate(self, attrs):
        data = super(TicketSerializer, self).validate(attrs)
        Ticket.validate_seat(
            attrs["seat"],
            attrs["trip"].trip.bus.num_seats,
            serializers.ValidationError
        )
        return data

        # if not (1 <= attrs["seat"] <= attrs["trip"].bus.num_seats):
        #     raise serializers.ValidationError(
        #         {
        #             "seat": f"seat must be in range [1, {attrs['trip'].bus.num_seats}], not {attrs['seat']}"
        #         }
        #     )


class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Order
        fields = ["id", "created_at", "tickets"]

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            order = Order.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(order=order, **ticket_data)
            return order

