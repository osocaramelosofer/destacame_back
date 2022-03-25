from rest_framework import serializers
from ..models import Passenger, Driver
# from buses.api.serializers import BussRouteSerializer
# import buses.api.serializers as perro


class PassengerSerializer(serializers.ModelSerializer):
    # leg = perro.BussRouteSerializer()

    class Meta:
        model = Passenger
        fields = ['id', 'name', 'leg']

    # def get_leg(self, obj):
    #     return AuthorSerializer(obj.author).data


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ['id', 'name']
