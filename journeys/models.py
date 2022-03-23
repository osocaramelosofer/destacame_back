from django.db import models


class Journey(models.Model):
    departure = models.CharField(max_length=255, blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.destination}'
