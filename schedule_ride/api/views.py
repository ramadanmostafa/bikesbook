from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

import schedule_ride
from .serializers import ScheduleRideSerializer, ScheduleRideRequestSerializer
from places.api.permissions import IsAuthenticated
from .permissions import IsSheduleRideOwner
from ..models import ScheduleRide, ScheduleRideMembership, ScheduleRideJoiningRequests
from garage.models import Motorcycle, Bicycle

class ScheduleRideListAPIView(ListAPIView):
    '''
         list of current user saved Schedule rides
    '''
    serializer_class = ScheduleRideSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return ScheduleRide.objects.filter(user=self.request.user)

class AddNewScheduleRideCreateAPIView(CreateAPIView):
    """
    Add a new record to my Schedule rides table
    """
    serializer_class = ScheduleRideSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():

            new_schedule_ride = ScheduleRide(
                start_location_lat=serializer.data["start_location_lat"],
                start_location_lng=serializer.data["start_location_lng"],
                start_location_city=serializer.data["start_location_city"],
                start_date=serializer.data["start_date"],
                start_time=serializer.data["start_time"],
                allow_bikers_join=serializer.data["allow_bikers_join"],
                bicycle=None if serializer.data["bicycle"] is None else Bicycle.objects.get(id=serializer.data["bicycle"]),
                motorcycle=None if serializer.data["motorcycle"] is None else Motorcycle.objects.get(id=serializer.data["motorcycle"])
            )
            new_schedule_ride.save()
            ScheduleRideMembership.objects.create(is_admin=True, schedule_ride_id=new_schedule_ride.id, user_id=request.user.id)

            return Response(ScheduleRideSerializer(new_schedule_ride).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteMyScheduleRideDestroyAPIView(DestroyAPIView):
    """
    delete the selected Schedule Ride 
    """
    queryset = ScheduleRide.objects.all()
    lookup_field = 'pk'
    serializer_class = ScheduleRideSerializer
    permission_classes = [IsAuthenticated, IsSheduleRideOwner]

class UpdateMyScheduleRideAPIView(RetrieveUpdateAPIView):
    """
    update my Schedule ride
    """
    queryset = ScheduleRide.objects.all()
    lookup_field = 'pk'
    serializer_class = ScheduleRideSerializer
    permission_classes = [IsAuthenticated, IsSheduleRideOwner]

class ScheduleRidesNearMeListAPIView(ListAPIView):
    """
    get all the rides at the same city excluding rides the requested user joined
    """
    serializer_class = ScheduleRideSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return ScheduleRide.objects.filter(
            allow_bikers_join=True,
            start_location_city=self.kwargs["city"]
        ).exclude(
            user=self.request.user
        )

class AddRequestScheduleRide(CreateAPIView):
    """
    Add a new request to join a specific schedule ride with status P (ending)
    if the request exists, return -1
    """
    serializer_class = ScheduleRideRequestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not ScheduleRideJoiningRequests.objects.filter(from_user=request.user,schedule_ride=request.data["schedule_ride"]):
                new_request = ScheduleRideJoiningRequests(
                    from_user=request.user,
                    schedule_ride=ScheduleRide.objects.get(id=request.data["schedule_ride"]),
                    request_status="P"
                )
                new_request.save()
                return Response(ScheduleRideRequestSerializer(new_request).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"code": -1, "message": "request Already sent"}, status=status.HTTP_400_BAD_REQUEST)


        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListRequestsIMade(ListAPIView):
    """
    get all schedule rides joining requests i sent to others
    """
    serializer_class = ScheduleRideSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):

        return ScheduleRide.objects.filter(
            scheduleridejoiningrequests__from_user=self.request.user,
            scheduleridejoiningrequests__request_status="P"
        )
