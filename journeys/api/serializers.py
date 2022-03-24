from rest_framework import serializers

from ..models import Journey

from routes.api.serializers import RouteSerializer
from passengers.api.serializers import DriverSerializer, PassengerSerializer
from buses.api.serializers import BussSerializer


class JourneySerializer(serializers.ModelSerializer):

    route = RouteSerializer()
    buss = BussSerializer()
    passenger = PassengerSerializer()
    driver = DriverSerializer()

    class Meta:
        model = Journey
        fields = ['id', 'route', 'buss', 'passenger', 'driver', 'date', 'time']

    # def create(self, validated_data):
    #     route = validated_data.pop('route')
    #     buss = validated_data.pop('buss')
    #     passenger = validated_data.pop('passenger')
    #     driver = validated_data.pop('driver')
    #
    #     print(route)
    #     print(buss)
    #     print(passenger)
    #     print(driver)
    #
    #     return Journey.objects.create(**validated_data)
