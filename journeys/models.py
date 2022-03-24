from django.db import models

from buses.models import Buss
from passengers.models import Passenger, Driver
from routes.models import Route


class Journey(models.Model):
    route = models.ForeignKey('routes.Route', on_delete=models.CASCADE, null=True, blank=True)
    buss = models.ForeignKey('buses.Buss', on_delete=models.CASCADE, null=True, blank=True)
    passenger = models.ForeignKey('passengers.Passenger', on_delete=models.CASCADE, null=True, blank=True)
    driver = models.ForeignKey('passengers.Driver', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True, blank=True)

    time = models.TimeField(null=True)

    def __str__(self):
        return f'{self.route}'
