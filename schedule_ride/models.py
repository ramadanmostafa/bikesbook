from __future__ import unicode_literals

from django.db import models
from garage.models import Bicycle, Motorcycle
from custom_user.models import CustomUser


class ScheduleRide(models.Model):

    start_location_lat = models.FloatField()
    start_location_lng = models.FloatField()
    start_location_city = models.CharField(max_length=120)
    start_date = models.DateField()
    start_time = models.TimeField()
    allow_bikers_join = models.BooleanField(default=False)
    user = models.ManyToManyField(CustomUser, through='ScheduleRideMembership')

    def __str__(self):
        return str(self.user) + "Schedule Ride On:" + str(self.start_date)

class ScheduleRideMembership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    schedule_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    bicycle = models.ForeignKey(Bicycle, blank=True, null=True, on_delete=models.CASCADE)
    motorcycle = models.ForeignKey(Motorcycle, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + str(self.schedule_ride)

class ScheduleRideJoiningRequests(models.Model):

    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender", null=True)
    schedule_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="receiver", null=True)

    REQUEST_CHOICES = (
        ('P', 'Pending'),
        ('D', 'Denied'),
        ('A', 'Approved'),
        ('C', 'Cancelled'),
    )
    request_status = models.CharField(max_length=1, choices=REQUEST_CHOICES, null=True)
    bicycle = models.ForeignKey(Bicycle, blank=True, null=True, on_delete=models.CASCADE)
    motorcycle = models.ForeignKey(Motorcycle, blank=True, null=True, on_delete=models.CASCADE)
