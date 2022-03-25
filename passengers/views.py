from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .api.serializers2 import PassengerSerializer
from .models import Passenger
from buses.models import BussRoute
from buses.api.serializers import BussRouteSerializer


@api_view(['POST'])
def create_passenger(request):
    if request.method == 'POST':
        name = request.data['name']
        leg_id = request.data['leg']['id']

        passenger_instance = Passenger.objects.create(name=name)
        leg_instance = BussRoute.objects.filter(id=leg_id).first()
        passenger_instance.leg = leg_instance
        passenger_instance.save()

        serializer = PassengerSerializer(passenger_instance)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def update_passenger(request):
    passenger_id = request.data['id']
    leg_id = request.data['leg']['id']
    name = request.data['name']

    leg_instance = BussRoute.objects.filter(id=leg_id).first()
    passenger_instance = Passenger.objects.filter(id=passenger_id).first()

    passenger_instance.name = name
    passenger_instance.leg = leg_instance
    passenger_instance.save()

    serializer = PassengerSerializer(passenger_instance)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
