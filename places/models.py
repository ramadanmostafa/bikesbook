from __future__ import unicode_literals
from custom_user.models import CustomUser

from django.db import models


class MyPlaces(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=120)
    location_lat = models.FloatField()
    location_lng = models.FloatField()

