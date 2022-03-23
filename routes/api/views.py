from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .serializers import RouteSerializer
from ..models import Route


class RouteModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Route.objects.all()
    serializer_class = RouteSerializer