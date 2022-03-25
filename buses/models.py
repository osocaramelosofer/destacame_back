from django.db import models
from django.urls import reverse
from passengers.models import Driver


class Buss(models.Model):
    plate = models.CharField(max_length=12, blank=True, null=True)
    driver = models.ForeignKey('passengers.Driver', on_delete=models.CASCADE, related_name='driver_buss', blank=True, null=True)
    seats = models.ManyToManyField('buses.Seat', blank=True)

    def __str__(self):
        return f'ID: {self.pk} - Plate:{self.plate}'


class BussRoute(models.Model):
    route = models.ForeignKey('routes.Route', on_delete=models.CASCADE, related_name='route_buss_route', blank=True, null=True)
    buss = models.ForeignKey('buses.Buss', on_delete=models.CASCADE, related_name='buss_buss_route', blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return f'{self.route} - {self.date}'


class Seat(models.Model):
    SEAT_CHOICES = [
        ('A', 'Seat A'),
        ('B', 'Seat B'),
        ('C', 'Seat C'),
        ('D', 'Seat D'),
        ('E', 'Seat E'),
        ('F', 'Seat F'),
        ('G', 'Seat G'),
        ('H', 'Seat H'),
        ('I', 'Seat I'),
        ('J', 'Seat J'),
    ]

    name = models.CharField(max_length=50, blank=True, null=True, choices=SEAT_CHOICES)

    def __str__(self):
        return f'{self.name}'
