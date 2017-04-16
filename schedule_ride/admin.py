from django.contrib import admin
from .models import ScheduleRideJoiningRequests, ScheduleRide, ScheduleRideMembership
# Register your models here.
admin.site.register(ScheduleRideMembership)
admin.site.register(ScheduleRide)
admin.site.register(ScheduleRideJoiningRequests)