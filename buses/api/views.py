from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import BussSerializer
from ..models import Buss


class BussModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Buss.objects.all()
    serializer_class = BussSerializer
