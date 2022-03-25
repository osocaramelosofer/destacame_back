from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import BussSerializer, BussRouteSerializer
from ..models import Buss, BussRoute


class BussModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Buss.objects.all()
    serializer_class = BussSerializer


class BussRouteModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = BussRoute.objects.all()
    serializer_class = BussRouteSerializer
