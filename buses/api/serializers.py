from rest_framework import serializers

from passengers.models import Driver
from passengers.api.serializers import DriverSerializer
from ..models import Buss


class BussSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = Buss
        fields = ['id', 'plate', 'driver']

    def create(self, validated_data):
        print("Validated data =>", validated_data)
        driver = validated_data.pop('driver')
        print('Driver Name =', driver['name'])
        print('Driver Name =', driver['id'])
        print("Driver => ", driver)

        buss_instance = Buss.objects.create(**validated_data)

        # for driver_data in driver:

        return buss_instance
