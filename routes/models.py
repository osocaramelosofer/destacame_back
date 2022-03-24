from django.db import models


class Route(models.Model):
    origin = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.origin} - {self.destination}'
