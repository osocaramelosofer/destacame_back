from django.db import models
from django.urls import reverse


class Route(models.Model):
    origin = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.destination}'

    def get_absolute_url(self):
        return reverse('routes:detail_route', args=[str(self.id)])
