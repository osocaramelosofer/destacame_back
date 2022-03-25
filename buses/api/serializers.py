from rest_framework import serializers

from passengers.api.serializers import DriverSerializer
from routes.api.serializers import RouteSerializer
from ..models import Buss, BussRoute


class BussSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = Buss
        fields = ['id', 'plate', 'driver']

    # def create(self, validated_data):
    #     print("Validated data =>", validated_data)
    #     driver = validated_data.pop('driver')
    #     print('Driver Name =', driver['name'])
    #     print('Driver Name =', driver['id'])
    #     print("Driver => ", driver)
    #
    #     buss_instance = Buss.objects.create(**validated_data)
    #
    #
    #
    #     return buss_instance


class BussRouteSerializer(serializers.ModelSerializer):
    route = RouteSerializer() # Origin & destination
    buss = BussSerializer()

    class Meta:
        model = BussRoute
        fields = ['id', 'route', 'buss', 'date', 'time']


