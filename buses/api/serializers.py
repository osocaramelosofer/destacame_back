from rest_framework import serializers

from ..models import Buss


class BussSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buss
        fields = ['id', 'plate', 'name']
