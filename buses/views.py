from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.utils import json
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .api.serializers import BussSerializer, BussRouteSerializer
from .models import Buss, BussRoute
from passengers.models import Driver
from routes.models import Route

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


@api_view(['POST'])
def update_buss(request):
    print('request.data ====', request.data)
    buss_id = request.data['id']
    plate = request.data['plate']
    driver_id = request.data['driver']['id']

    buss_instance = Buss.objects.filter(id=buss_id).first()

    print("buss instance ====>", buss_instance)

    driver_instance = Driver.objects.filter(id=driver_id).first()

    buss_instance.plate = plate
    buss_instance.driver = driver_instance
    buss_instance.save()

    serializer = BussSerializer(buss_instance)
    print("Buss serialized data", serializer.data)


    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_buss_route(request):

    if request.method == 'POST':
        route_id = request.data['route']['id']
        buss_id = request.data['buss']['id']
        date = request.data['date']
        time = request.data['time']

        buss_route_instance = BussRoute.objects.create(date=date, time=time)
        route_instance = Route.objects.filter(id=route_id).first()
        buss_instance = Buss.objects.filter(id=buss_id).first()

        buss_route_instance.route = route_instance
        buss_route_instance.buss = buss_instance

        buss_route_instance.save()

        serializer = BussRouteSerializer(buss_route_instance)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def update_buss_route(request):
    buss_route_id = request.data['id']
    route_id = request.data['route']['id']
    buss_id = request.data['buss']['id']
    date = request.data['date']
    time = request.data['time']

    buss_route_instance = BussRoute.objects.filter(id=buss_route_id).first()
    route_instance = Route.objects.filter(id=route_id).first()
    buss_instance = Buss.objects.filter(id=buss_id).first()

    buss_route_instance.route = route_instance
    buss_route_instance.buss = buss_instance
    buss_route_instance.date = date
    buss_route_instance.time = time

    buss_route_instance.save()

    serializer = BussRouteSerializer(buss_route_instance)

    return Response(data=serializer.data, status=status.HTTP_200_OK)