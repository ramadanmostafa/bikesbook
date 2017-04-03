from rest_framework import serializers
from ..models import ScheduleRide, ScheduleRideJoiningRequests


class ScheduleRideSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if "bicycle" not in data and "motorcycle" in data:
            data.update({"bicycle": None})
        elif "motorcycle" not in data and "bicycle" in data:
            data.update({"motorcycle": None})
        elif "motorcycle" in data and "bicycle" in data:
            raise serializers.ValidationError("You should select bicycle or motorcycle not both")
        else:
            raise serializers.ValidationError("You should select bicycle or motorcycle")

        return data

    class Meta:

        model = ScheduleRide
        fields = [
            "id",
            "start_location_lat",
            "start_location_lng",
            "start_location_city",
            "start_date",
            "start_time",
            "allow_bikers_join",
            "bicycle",
            "motorcycle",
        ]

class ScheduleRideRequestSerializer(serializers.ModelSerializer):


    class Meta:
        model = ScheduleRideJoiningRequests
        fields = [
            "schedule_ride",
            "from_user",
            "request_status"
        ]