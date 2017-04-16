from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScheduleRideSerializer, ScheduleRideRequestSerializer, \
    ScheduleRideListSerializer, ScheduleRideNearMeSerializer, ListRequestsToMeSerializer, JoinedBikersSerializer
from places.api.permissions import IsAuthenticated
from .permissions import IsSheduleRideOwner
from ..models import ScheduleRide, ScheduleRideMembership, ScheduleRideJoiningRequests
from custom_user.models import CustomUser
from garage.models import Motorcycle, Bicycle
from datetime import datetime


class ScheduleRideList(ListAPIView):
    '''
    list of current user saved Schedule rides
    start date should be greater than or equal to today's date
    '''
    serializer_class = ScheduleRideListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):

        rides = ScheduleRide.objects.filter(user=self.request.user, start_date__gte=datetime.now())
        data = []
        for ride in rides:
            temp_dict = dict()
            temp_dict["id"] = ride.id
            temp_dict["start_location_city"] = ride.start_location_city
            temp_dict["start_date"] = ride.start_date
            temp_dict["start_time"] = ride.start_time

            bicycle = ScheduleRideMembership.objects.filter(
                schedule_ride=ride,
                is_admin=True
            ).exclude(
                bicycle=None
            )

            if len(bicycle) == 1:
                bike = dict()
                bicycle = bicycle[0].bicycle
                bike["id"] = bicycle.id
                bike["color"] = bicycle.color
                bike["make"] = bicycle.make.brand
                bike["style"] = bicycle.style.style
                temp_dict["bicycle"] = bike
            else:
                temp_dict["bicycle"] = None

            motorbike = ScheduleRideMembership.objects.filter(
                schedule_ride=ride,
                is_admin=True
            ).exclude(
                motorcycle=None
            )

            if len(motorbike) == 1:
                motorcycle = dict()
                motorbike = motorbike[0].motorcycle
                motorcycle["id"] = motorbike.id
                motorcycle["color"] = motorbike.color
                motorcycle["make"] = motorbike.make.brand
                motorcycle["model"] = motorbike.model.model
                motorcycle["style"] = motorbike.style.style
                motorcycle["engine_size"] = motorbike.engine_size.cc
                temp_dict["motorcycle"] = motorcycle
            else:
                temp_dict["motorcycle"] = None

            temp_dict["is_admin"] = ScheduleRideMembership.objects.get(
                schedule_ride=ride,
                user=self.request.user
            ).is_admin

            temp_dict["admin_mobile_number"] = ''
            if temp_dict["is_admin"]:
                temp_dict["admin_mobile_number"] = CustomUser.objects.get(
                    scheduleridemembership__schedule_ride=ride,
                    scheduleridemembership__is_admin=True
                ).mobile_number

            requests = dict()
            requests["total_number"] = len(ScheduleRideJoiningRequests.objects.filter(schedule_ride=ride))
            requests["pending"] = len(ScheduleRideJoiningRequests.objects.filter(schedule_ride=ride, request_status="P"))
            requests["approved"] = len(ScheduleRideJoiningRequests.objects.filter(schedule_ride=ride, request_status="A"))
            requests["denied"] = len(ScheduleRideJoiningRequests.objects.filter(schedule_ride=ride, request_status="D"))
            temp_dict["requests"] = requests
            data.append(temp_dict)
        return data


class AddNewScheduleRideCreateAPIView(CreateAPIView):
    """
    Add a new record to my Schedule rides table
    """
    serializer_class = ScheduleRideSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not ScheduleRide.objects.filter(
                start_date=serializer.data["start_date"],
                start_time=serializer.data["start_time"]
            ):
                new_schedule_ride = ScheduleRide(
                    start_location_lat=serializer.data["start_location_lat"],
                    start_location_lng=serializer.data["start_location_lng"],
                    start_location_city=serializer.data["start_location_city"],
                    start_date=serializer.data["start_date"],
                    start_time=serializer.data["start_time"],
                    allow_bikers_join=serializer.data["allow_bikers_join"]
                )
                new_schedule_ride.save()
                ScheduleRideMembership.objects.create(
                    is_admin=True,
                    schedule_ride_id=new_schedule_ride.id,
                    user_id=request.user.id,
                    bicycle=None if serializer.data["bicycle"] is None else Bicycle.objects.get(
                        id=serializer.data["bicycle"]
                    ),
                    motorcycle=None if serializer.data["motorcycle"] is None else Motorcycle.objects.get(
                        id=serializer.data["motorcycle"]
                    )
                )
                return Response(
                    ScheduleRideSerializer(
                        new_schedule_ride
                    ).data,
                    status=status.HTTP_201_CREATED
                )

            else:
                body = {
                    "code": -1,
                    "message": "you have another ride at the same time"
                }
                return Response(
                    body,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


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
    serializer_class = ScheduleRideNearMeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        rides = ScheduleRide.objects.filter(
            allow_bikers_join=True,
            start_location_city=self.kwargs["city"],
            start_date__gte=datetime.now()
        ).exclude(
            user=self.request.user
        )

        data = []
        for ride in rides:
            temp_dict = dict()
            temp_dict["id"] = ride.id
            temp_dict["start_location_city"] = ride.start_location_city
            temp_dict["start_date"] = ride.start_date
            temp_dict["start_time"] = ride.start_time
            temp_dict["admin_name"] = ScheduleRideMembership.objects.get(
                is_admin=True,
                schedule_ride=ride
            ).user.full_name

            bicycle = ScheduleRideMembership.objects.filter(
                schedule_ride=ride,
                is_admin=True
            ).exclude(
                bicycle=None
            )

            if len(bicycle) == 1:
                bike = dict()
                bicycle = bicycle[0].bicycle
                bike["id"] = bicycle.id
                bike["color"] = bicycle.color
                bike["make"] = bicycle.make.brand
                bike["style"] = bicycle.style.style
                temp_dict["bicycle"] = bike
            else:
                temp_dict["bicycle"] = None

            motorbike = ScheduleRideMembership.objects.filter(
                schedule_ride=ride,
                is_admin=True
            ).exclude(
                motorcycle=None
            )

            if len(motorbike) == 1:
                motorcycle = dict()
                motorbike = motorbike[0].motorcycle
                motorcycle["id"] = motorbike.id
                motorcycle["color"] = motorbike.color
                motorcycle["make"] = motorbike.make.brand
                motorcycle["model"] = motorbike.model.model
                motorcycle["style"] = motorbike.style.style
                motorcycle["engine_size"] = motorbike.engine_size.cc
                temp_dict["motorcycle"] = motorcycle
            else:
                temp_dict["motorcycle"] = None
            #############################################################################
            temp_dict["start_location_lng"] = ride.start_location_lng
            temp_dict["start_location_lat"] = ride.start_location_lat
            data.append(temp_dict)
        return data


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
            if not ScheduleRideJoiningRequests.objects.filter(
                from_user=request.user,
                schedule_ride=request.data["schedule_ride"]
            ):
                to_user = ScheduleRideMembership.objects.get(
                            schedule_ride=request.data["schedule_ride"],
                            is_admin=True
                ).user
                if request.user != to_user:
                    # TODO get default bike (motorcycle or bicycle) and insert it to ScheduleRideJoiningRequests table
                    motorcycle = None
                    bicycle = None
                    try:
                        motorcycle = Motorcycle.objects.get(
                            garage__user=request.user,
                            default=True
                        )
                    except:
                        try:
                            bicycle = Bicycle.objects.get(
                                garage__user=request.user,
                                default=True
                            )
                        except:
                            body = {
                                "code": -2,
                                "message": "You should choose a default bike first"
                            }
                            return Response(
                                body,
                                status=status.HTTP_400_BAD_REQUEST
                            )

                    new_request = ScheduleRideJoiningRequests(
                        from_user=request.user,
                        schedule_ride=ScheduleRide.objects.get(id=request.data["schedule_ride"]),
                        request_status="P",
                        to_user=to_user,
                        bicycle=bicycle,
                        motorcycle=motorcycle
                    )
                    new_request.save()
                    return Response(
                        ScheduleRideRequestSerializer(
                            new_request
                        ).data,
                        status=status.HTTP_201_CREATED
                    )
                else:
                    body = {
                        "code": -1,
                        "message": "You can't send request to yourself"
                    }
                    return Response(
                        body,
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                body = {
                    "code": -1,
                    "message": "request Already sent"
                }
                return Response(
                    body,
                    status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class ListRequestsIMade(ListAPIView):
    """
    get all schedule rides joining requests i sent to others
    id --> is the request id not the ride it, use it to cancel this request
    """
    serializer_class = ScheduleRideNearMeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):

        rides = ScheduleRide.objects.filter(
            scheduleridejoiningrequests__from_user=self.request.user,
            scheduleridejoiningrequests__request_status="P"
        )
        data = []
        for ride in rides:
            temp_dict = dict()
            temp_dict["id"] = ScheduleRideJoiningRequests.objects.get(
                schedule_ride=ride,
                from_user=self.request.user,
                request_status="P"
            ).pk
            temp_dict["start_location_city"] = ride.start_location_city
            temp_dict["start_date"] = ride.start_date
            temp_dict["start_time"] = ride.start_time
            temp_dict["admin_name"] = ScheduleRideMembership.objects.get(
                is_admin=True,
                schedule_ride=ride
            ).user.full_name

            bicycle = ScheduleRideMembership.objects.filter(
                schedule_ride=ride,
                is_admin=True
            ).exclude(
                bicycle=None
            )

            if len(bicycle) == 1:
                bike = dict()
                bicycle = bicycle[0].bicycle
                bike["id"] = bicycle.id
                bike["color"] = bicycle.color
                bike["make"] = bicycle.make.brand
                bike["style"] = bicycle.style.style
                temp_dict["bicycle"] = bike
            else:
                temp_dict["bicycle"] = None

            motorbike = ScheduleRideMembership.objects.filter(
                schedule_ride=ride,
                is_admin=True
            ).exclude(
                motorcycle=None
            )

            if len(motorbike) == 1:
                motorcycle = dict()
                motorbike = motorbike[0].motorcycle
                motorcycle["id"] = motorbike.id
                motorcycle["color"] = motorbike.color
                motorcycle["make"] = motorbike.make.brand
                motorcycle["model"] = motorbike.model.model
                motorcycle["style"] = motorbike.style.style
                motorcycle["engine_size"] = motorbike.engine_size.cc
                temp_dict["motorcycle"] = motorcycle
            else:
                temp_dict["motorcycle"] = None
            #############################################################################
            temp_dict["start_location_lng"] = ride.start_location_lng
            temp_dict["start_location_lat"] = ride.start_location_lat
            data.append(temp_dict)
        return data


class ListRequestsToMe(ListAPIView):
    """
    get (GET Request) all schedule rides joining requests sent to the current user
    
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ListRequestsToMeSerializer

    def get_queryset(self):

        rides = ScheduleRide.objects.filter(
            scheduleridemembership__is_admin=True,
            scheduleridemembership__user=self.request.user,
            scheduleridejoiningrequests__request_status="P"
        )
        data = []
        for ride in rides:
            joining_requests = ScheduleRideJoiningRequests.objects.filter(
                schedule_ride=ride
            )
            for joining_request in joining_requests:
                data.append(
                    {
                        "request_id": joining_request.id,
                        "request_sender_full_name": joining_request.from_user.full_name,
                        "start_date": ride.start_date,
                        "start_time": ride.start_time,
                        "start_location_lng": ride.start_location_lng,
                        "start_location_lat": ride.start_location_lat
                    }
                )

        return data


class AcceptRequestAPIView(UpdateAPIView):
    """
        should be called if the admin of the schedule ride wants to accept someone's request
    """
    queryset = ScheduleRideJoiningRequests.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsSheduleRideOwner]

    def update(self, request, *args, **kwargs):
        try:
            my_request = ScheduleRideJoiningRequests.objects.get(
                id=self.kwargs["pk"]
            )
        except:
            body = {
                "code":-1,
                "message": "Request Not Found"
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )

        if my_request.request_status != "P":
            body = {
                "code": "-2",
                "message": "Request status should be P Not %s" % my_request.request_status
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )
        if not ScheduleRideMembership.objects.filter(
                is_admin=True,
                schedule_ride=my_request.schedule_ride,
                user=request.user
        ):
            body = {
                "code": "-3",
                "message": "You should be the admin of this ride"
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )
        my_request.request_status = "A"
        my_request.save()
        ScheduleRideMembership.objects.get_or_create(
            is_admin=False,
            schedule_ride=my_request.schedule_ride,
            user_id=my_request.from_user.pk,
            bicycle=my_request.bicycle,
            motorcycle=my_request.motorcycle
        )
        body = {
            "code": 1,
            "message": "OK"
        }
        return Response(
            body,
            status=status.HTTP_200_OK
        )


class IgnoreRequestAPIView(UpdateAPIView):
    """
    should be called if the admin of the schedule ride wants to ignore someone's request
    """
    queryset = ScheduleRideJoiningRequests.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsSheduleRideOwner]

    def update(self, request, *args, **kwargs):
        try:
            my_request = ScheduleRideJoiningRequests.objects.get(id=self.kwargs["pk"])
        except ScheduleRideJoiningRequests.DoesNotExist:
            body = {
                "code": -1,
                "message": "Request Not Found"
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )
        if my_request.request_status != "P":
            body = {
                "code": "-2",
                "message": "Request status should be P Not %s" % my_request.request_status
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )

        if not ScheduleRideMembership.objects.filter(
            is_admin=True,
            schedule_ride=my_request.schedule_ride,
            user=request.user
        ):
            body = {
                "code": "-3",
                "message": "You should be the admin of this ride"
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )
        my_request.request_status = "I"
        my_request.save()
        body = {
            "code": 1,
            "message": "OK"
        }
        return Response(
            body,
            status=status.HTTP_200_OK
        )


class CancelReqIMade(UpdateAPIView):
    """
    should be called if a request sender want to cancel his request. will delete the record from the db
    """
    queryset = ScheduleRideJoiningRequests.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsSheduleRideOwner]

    def update(self, request, *args, **kwargs):
        try:
            my_request = ScheduleRideJoiningRequests.objects.get(id=self.kwargs["pk"])
        except ScheduleRideJoiningRequests.DoesNotExist:
            body = {
                "code": -1,
                "message": "Request Not Found"
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )
        if my_request.request_status != "P":
            body = {
                "code": "-2",
                "message": "Request status should be P Not %s" % my_request.request_status
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )
        if not ScheduleRideJoiningRequests.objects.filter(
            schedule_ride=my_request.schedule_ride,
            from_user=request.user
        ):
            body = {
                "code": "-3",
                "message": "You should be the sender of this request"
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )
        my_request.delete()
        body = {
            "code": 1,
            "message": "OK"
        }
        return Response(
            body,
            status=status.HTTP_200_OK
        )


class CheckJoinedBikers(ListAPIView):
    """
    should be called if the schedule ride admin wants to get a list of joined bikers
    """
    permission_classes = [IsAuthenticated]
    serializer_class = JoinedBikersSerializer

    def get_queryset(self):

        memberships = ScheduleRideMembership.objects.filter(
            schedule_ride=self.kwargs["pk"],
            is_admin=False
        )

        data = []
        for membership in memberships:
            temp_dict = dict()
            temp_dict["full_name"] = membership.user.full_name
            temp_dict["country_code"] = membership.user.country_code
            temp_dict["mobile_number"] = membership.user.mobile_number
            temp_dict["address"] = membership.user.address

            if membership.bicycle:
                bike = dict()
                bike["id"] = membership.bicycle.id
                bike["color"] = membership.bicycle.color
                bike["make"] = membership.bicycle.make.brand
                bike["style"] = membership.bicycle.style.style
                temp_dict["bicycle"] = bike
            else:
                temp_dict["bicycle"] = None

            if membership.motorcycle:
                motorcycle = dict()
                motorcycle["id"] = membership.motorcycle.id
                motorcycle["color"] = membership.motorcycle.color
                motorcycle["make"] = membership.motorcycle.make.brand
                motorcycle["model"] = membership.motorcycle.model.model
                motorcycle["style"] = membership.motorcycle.style.style
                motorcycle["engine_size"] = membership.motorcycle.engine_size.cc
                temp_dict["motorcycle"] = motorcycle
            else:
                temp_dict["motorcycle"] = None
            data.append(temp_dict)
        return data


class CancelJoiningScheduleRide(DestroyAPIView):
    """
    take id of a schedule ride that i joined but i am not the admin \n
    delete the request and the membership records for this user related to this ride 
    """
    def destroy(self, request, *args, **kwargs):
        current_user = self.request.user
        current_ride_id = self.kwargs["pk"]
        if not ScheduleRide.objects.filter(pk=current_ride_id):
            body = {
                "code": -1,
                "message": "Ride Does not exists"
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )

        current_membership = ScheduleRideMembership.objects.filter(
            schedule_ride=current_ride_id,
            user=current_user
        )

        if not current_membership:
            body = {
                "code": -2,
                "message": "You are not a member in this ride"
            }
            return Response(
                body,
                status=status.HTTP_400_BAD_REQUEST
            )

        if current_membership[0].is_admin:
            body = {
                "code": -3,
                "message": "You are the admin of this ride"
            }
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        current_joining_req = ScheduleRideJoiningRequests.objects.filter(
            from_user=current_user,
            schedule_ride=current_ride_id, request_status="A"
        )
        if not current_joining_req:
            body = {
                "code": -2,
                "message": "You are not a member in this ride"
            }
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        current_membership.delete()
        current_joining_req.delete()
        body = {
            "code": 1,
            "message": "Good"
        }
        return Response(
            body,
            status=status.HTTP_200_OK
        )
