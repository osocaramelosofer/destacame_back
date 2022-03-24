from django.urls import path
from .views import create_buss

urlpatterns = [
    path('create', create_buss, name='create_buss_def')
]