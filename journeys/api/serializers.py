from rest_framework import serializers

from ..models import Journey
# from destacame.config.buses.api.serializers import BussSerializer
from routes.api.serializers import RouteSerializer
from passengers.api.serializers import DriverSerializer, PassengerSerializer


class JourneySerializer(serializers.ModelSerializer):

    route = RouteSerializer()
    # buss = BussSerializer()
    passenger = PassengerSerializer()
    driver = DriverSerializer()

    class Meta:
        model = Journey
        fields = ['id', 'route', 'buss', 'passenger', 'driver', 'date', 'time']
