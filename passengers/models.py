from django.db import models
from django.contrib.auth.models import User


class Passenger(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Driver(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

