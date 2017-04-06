from rest_framework.permissions import BasePermission
from schedule_ride.models import ScheduleRideMembership

class IsSheduleRideOwner(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        temp = ScheduleRideMembership.objects.filter(user=request.user, schedule_ride__id=obj.id, is_admin=True)
        return len(temp) > 0

