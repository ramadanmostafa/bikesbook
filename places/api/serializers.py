from rest_framework import serializers
from places.models import MyPlaces


class MyPlacesSerializer(serializers.ModelSerializer):

    location_name = serializers.CharField()
    location_lat = serializers.CharField()
    location_lng = serializers.CharField()

    class Meta:

        model = MyPlaces
        fields = [
            "id",
            "location_name",
            "location_lat",
            "location_lng",
        ]
