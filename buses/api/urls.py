from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BussModelViewSet


router = DefaultRouter()
router.register('buss', BussModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
