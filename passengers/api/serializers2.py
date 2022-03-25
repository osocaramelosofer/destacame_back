from rest_framework import serializers
from ..models import Passenger
from buses.api.serializers import BussRouteSerializer


class PassengerSerializer(serializers.ModelSerializer):
    leg = BussRouteSerializer()

    class Meta:
        model = Passenger
        fields = ['id', 'name', 'leg']