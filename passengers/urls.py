from django.urls import path
from .views import create_passenger, update_passenger

urlpatterns = [
    path('create-passenger', create_passenger, name='create_passenger'),
    path('update-passenger', update_passenger, name='update_passenger'),
]