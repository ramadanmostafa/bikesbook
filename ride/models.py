from __future__ import unicode_literals

from django.db import models
from custom_user.models import CustomUser
from garage.models import Bicycle, Motorcycle

# Create your models here.
class Ride(models.Model):
    user = models.ForeignKey(CustomUser)
    start_lat = models.FloatField()
    start_lng = models.FloatField()
    end_lat = models.FloatField(null=True)
    end_lng = models.FloatField(null=True)
    distance = models.CharField(max_length=60, null=True)
    duration = models.CharField(max_length=60, null=True)
    max_speed = models.CharField(max_length=60, null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    bicycle = models.ForeignKey(Bicycle, blank=True, null=True)
    motorcycle = models.ForeignKey(Motorcycle, blank=True, null=True)
    in_ride_now = models.BooleanField(default=False)
    path_file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True)
    start_place = models.CharField(max_length=120, null=True)
    end_place = models.CharField(max_length=120, null=True)
