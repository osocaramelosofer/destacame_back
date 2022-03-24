from django.db import models
from django.urls import reverse
from passengers.models import Driver


class Buss(models.Model):
    plate = models.CharField(max_length=12, blank=True, null=True)
    driver = models.ForeignKey('passengers.Driver', on_delete=models.CASCADE, related_name='driver_buss', blank=True, null=True)


    def __str__(self):
        return f'{self.driver}'
