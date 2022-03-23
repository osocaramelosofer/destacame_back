from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .serializers import PassengerSerializer, DriverSerializer
from ..models import Passenger, Driver


class PassengerModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class DriverModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    