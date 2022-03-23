from django.db import models
from django.urls import reverse


class Buss(models.Model):
    plate = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('buses:buss_detail', args=[str(self.id)])
