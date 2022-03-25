from django.urls import path
from .views import create_buss, update_buss, create_buss_route, update_buss_route

urlpatterns = [
    path('create', create_buss, name='create_buss_def'),
    path('update', update_buss, name='update_buss_def'),
    path('create-bussroute', create_buss_route, name='create_buss_route'),
    path('update-buss-route', update_buss_route, name='update_buss_route'),

]