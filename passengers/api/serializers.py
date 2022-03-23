from rest_framework import serializers
from ..models import Passenger, Driver


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = ['id', 'name']


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ['id', 'name']
