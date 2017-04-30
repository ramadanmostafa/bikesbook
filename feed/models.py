from __future__ import unicode_literals

from django.db import models
from custom_user.models import CustomUser
from garage.models import Bicycle, Motorcycle
from ride.models import Ride
from schedule_ride.models import ScheduleRide, ScheduleRideJoiningRequests
from places.models import MyPlaces


class Feeds(models.Model):
    feed_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owner")
    type = models.IntegerField()

    action_bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE, null=True)
    action_motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, null=True)
    action_ride = models.ForeignKey(Ride, on_delete=models.CASCADE, null=True)
    action_schedule_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE, null=True)
    action_request = models.ForeignKey(ScheduleRideJoiningRequests, on_delete=models.CASCADE, null=True)
    action_myplace = models.ForeignKey(MyPlaces, on_delete=models.CASCADE, null=True)

    created = models.DateTimeField(auto_now=True)

