from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Journey
from .serializers import JourneySerializer


class JourneyModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
