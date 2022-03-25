from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BussModelViewSet, BussRouteModelViewSet


router = DefaultRouter()
router.register('buss', BussModelViewSet)
router.register('buss-route', BussRouteModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
