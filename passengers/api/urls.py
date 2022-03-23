from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PassengerModelViewSet, DriverModelViewSet

router = DefaultRouter()

router.register('passenger', PassengerModelViewSet)
router.register('driver', DriverModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
