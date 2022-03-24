from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JourneyModelViewSet

router = DefaultRouter()

router.register('journey', JourneyModelViewSet)

urlpatterns =[
    path('', include(router.urls))
]