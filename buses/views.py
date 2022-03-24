from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.utils import json
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .api.serializers import BussSerializer
from .models import Buss
from passengers.models import Driver

@api_view(['POST'])
def create_buss(request):
    if request.method == 'POST':

        print('request.data ====', request.data)
        driver = request.data['driver']
        print("REQUEST DRIVER =>", driver)
        buss_instance = Buss.objects.create(plate=request.data['plate'])
        driver_instance = Driver.objects.filter(id=driver['id']).first()

        buss_instance.driver = driver_instance
        buss_instance.save()

        serializer = BussSerializer(buss_instance)
        print("Buss serialized data", serializer.data)


        return Response(data=serializer.data, status=status.HTTP_200_OK)
