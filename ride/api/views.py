from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from ride.models import Ride
from garage.api.permissions import IsGarageOwner
from ride.api.serializers import RideListSerializer, RideStartSerializer, RideEndSerializer, RideFileSerializer
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone

class RideStartAPIView(CreateAPIView):
    """
    start a new ride now, returns the ride id to be used when ending this ride
    this will change the in_ride_now flag to True and detect the ride start time automatically 
    """

    serializer_class = RideStartSerializer
    permission_classes = [IsGarageOwner]


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_ride = Ride(
                user=self.request.user,
                start_place=serializer.data["start_place"],
                motorcycle_id=serializer.data["motorcycle"],
                start_lat=serializer.data["start_lat"],
                start_lng=serializer.data["start_lng"],
                start_time=timezone.now(),
                in_ride_now=True
            )
            new_ride.save()
            response_data = RideStartSerializer(new_ride).data
            return Response(response_data, status=status.HTTP_200_OK)

class RideEndAPIView(RetrieveUpdateAPIView):
    """
    should be called at the end of each ride using ride id,
    this will change the in_ride_now flag to False and detect the ride end time automatically 
    """

    serializer_class = RideEndSerializer
    permission_classes = [IsGarageOwner]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            my_ride = Ride.objects.get(id=serializer.data["id"])
            my_ride.end_lat = serializer.data["end_lat"]
            my_ride.end_lng = serializer.data["end_lng"]
            my_ride.distance = serializer.data["distance"]
            my_ride.duration = serializer.data["duration"]
            my_ride.max_speed = serializer.data["max_speed"]
            my_ride.end_time = timezone.now()
            my_ride.in_ride_now = False
            my_ride.end_place = serializer.data["end_place"]
            my_ride.save()
            response_data = RideStartSerializer(my_ride).data
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RideFileAPIView(CreateAPIView):
    """
    receive a ride file and the id of the ride then store the file in media_cdn/uploads/Year/Month/Day
    """
    serializer_class = RideFileSerializer
    permission_classes = [IsGarageOwner]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            my_ride = Ride.objects.get(id=serializer.data["id"])
            my_ride.path_file = request.data.get("path_file")
            my_ride.save()
            return Response({"code": 1}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RideListAPIView(ListAPIView):
    '''
     list of current user Rides
    '''
    serializer_class = RideListSerializer
    permission_classes = [IsGarageOwner]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Ride.objects.filter(user=self.request.user)
        return queryset_list