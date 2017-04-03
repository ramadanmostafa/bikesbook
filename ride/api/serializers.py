from rest_framework import serializers
from ride.models import Ride

class RideStartSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if "bicycle" not in data and "motorcycle" in data:
            data.update({"bicycle":None})
        elif "motorcycle" not in data and "bicycle" in data:
            data.update({"motorcycle":None})
        elif "motorcycle" in data and "bicycle" in data:
            raise serializers.ValidationError("You should select bicycle or motorcycle not both")
        else:
            raise serializers.ValidationError("You should select bicycle or motorcycle")

        return data

    class Meta:
        model = Ride
        fields = [
            "id",
            "start_lat",
            "start_lng",
            "start_time",
            "bicycle",
            "motorcycle",
            "start_place",
            "in_ride_now",
        ]

class RideEndSerializer(serializers.ModelSerializer):

    id = serializers.CharField()
    end_lat = serializers.CharField()
    end_lng = serializers.CharField()
    distance = serializers.CharField()
    duration = serializers.CharField()
    max_speed = serializers.CharField()
    end_place = serializers.CharField()

    def validate(self, attrs):
        try:
            Ride.objects.get(id=attrs["id"])
        except:
            raise serializers.ValidationError("Wrong Ride ID")
        else:
            return attrs


    class Meta:
        model = Ride
        fields = [
            "id",
            "end_lat",
            "end_lng",
            "end_time",
            "distance",
            "duration",
            "max_speed",
            "end_place",
        ]

class RideFileSerializer(serializers.ModelSerializer):

    id = serializers.CharField()
    path_file = serializers.FileField()

    def validate(self, attrs):
        try:
            Ride.objects.get(id=int(attrs["id"]))
        except:
            raise serializers.ValidationError("Wrong Ride ID")
        else:
            return attrs

    class Meta:
        model = Ride
        fields = [
            "id",
            "path_file"
        ]



class RideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            "id",
            "user",
            "start_lat",
            "start_lng",
            "end_lat",
            "end_lng",
            "distance",
            "duration",
            "max_speed",
            "start_time",
            "end_time",
            "bicycle",
            "motorcycle",
            "in_ride_now",
            "path_file",
            "start_place",
            "end_place",
        ]
        extra_kwargs = {"id": {"read_only": True}}
