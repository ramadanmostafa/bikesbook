from rest_framework import serializers
from ..models import ScheduleRide, ScheduleRideJoiningRequests
from custom_user.models import CustomUser


class ScheduleRideSerializer(serializers.ModelSerializer):
    """
    
    """
    bicycle = serializers.IntegerField(allow_null=True, required=False)
    motorcycle = serializers.IntegerField(allow_null=True, required=False)

    def validate(self, data):
        if "bicycle" not in data and "motorcycle" in data:
            data.update(
                {
                    "bicycle": None
                }
            )
        elif "motorcycle" not in data and "bicycle" in data:
            data.update(
                {
                    "motorcycle": None
                }
            )
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
            "request_status",
            "to_user"
        ]

class RequestActionSerializer(serializers.Serializer):

    id = serializers.CharField(max_length=120, allow_blank=False)

    def validate(self, attrs):
        if not attrs["id"].isdigit():
            raise serializers.ValidationError(
                {
                    "id": "Should be a number"
                }
            )

        if not ScheduleRideJoiningRequests.objects.filter(id=attrs["id"]):
            raise serializers.ValidationError(
                {
                    'id': 'Request ID not found'
                }
            )
        return attrs


    class Meta:
        module = ScheduleRideJoiningRequests
        fields = [
            'id'
        ]

class ScheduleRideListSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField()
    requests = serializers.DictField()
    bicycle = serializers.DictField()
    motorcycle = serializers.DictField()
    admin_mobile_number = serializers.CharField(max_length=25)

    class Meta:

        model = ScheduleRide
        fields = [
            "id",
            "start_location_city",
            "start_date",
            "start_time",
            "is_admin",
            "bicycle",
            "motorcycle",
            "requests",
            "admin_mobile_number",
        ]

class ScheduleRideNearMeSerializer(serializers.ModelSerializer):
    admin_name = serializers.CharField()
    bicycle = serializers.DictField()
    motorcycle = serializers.DictField()

    class Meta:

        model = ScheduleRide
        fields = [
            "id",
            "start_location_city",
            "start_date",
            "start_time",
            "admin_name",
            "bicycle",
            "motorcycle",
            "start_location_lng",
            "start_location_lat",
        ]


class ListRequestsToMeSerializer(serializers.ModelSerializer):

    request_id = serializers.IntegerField()
    request_sender_full_name = serializers.CharField()

    class Meta:
        model = ScheduleRide
        fields = [
            "request_id",
            "request_sender_full_name",
            "start_date",
            "start_time",
            "start_location_lng",
            "start_location_lat"
        ]


class JoinedBikersSerializer(serializers.ModelSerializer):
    motorcycle = serializers.DictField()
    bicycle = serializers.DictField()

    class Meta:
        model = CustomUser
        fields = [
            "full_name",
            "motorcycle",
            "bicycle",
            "country_code",
            "mobile_number",
            "address"
        ]