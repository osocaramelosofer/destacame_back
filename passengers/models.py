from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Passenger(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('persons:passenger_detail', args=[str(self.id)])


class Driver(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('persons:driver_detail', args=[str(self.id)])
