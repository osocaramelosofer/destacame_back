from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import RouteModelViewSet

router = DefaultRouter()

router.register('route', RouteModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]