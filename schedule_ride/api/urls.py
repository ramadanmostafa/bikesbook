from django.conf.urls import url
from .views import ScheduleRideList, AddNewScheduleRideCreateAPIView, UpdateMyScheduleRideAPIView,\
    DeleteMyScheduleRideDestroyAPIView, ScheduleRidesNearMeListAPIView, AddRequestScheduleRide, ListRequestsIMade,\
    ListRequestsToMe, AcceptRequestAPIView, IgnoreRequestAPIView, CancelReqIMade, CheckJoinedBikers,\
    CancelJoiningScheduleRide


urlpatterns = [

    # list all my schedule rides
    url(
        regex=r'^$',
        view=ScheduleRideList.as_view(),
        name='list_my_schedule_rides'
    ),

    # add new schedule rides
    url(
        regex=r'^addnewscheduleride/$',
        view=AddNewScheduleRideCreateAPIView.as_view(),
        name='add_new_schedule_ride'
    ),

    # delete my schedule ride
    url(
        regex=r'^deletescheduleride/(?P<pk>[0-9]+)/$',
        view=DeleteMyScheduleRideDestroyAPIView.as_view(),
        name='delete_schedule_ride'
    ),

    # update my schedule ride
    url(
        regex=r'^updatescheduleride/(?P<pk>[0-9]+)/$',
        view=UpdateMyScheduleRideAPIView.as_view(),
        name='update_schedule_ride'
    ),

    # list schedule rides near me
    url(
        regex=r'^ridesnearme/(?P<city>[0-9a-zA-Z]+)/$',
        view=ScheduleRidesNearMeListAPIView.as_view(),
        name='rides_near_me'
    ),

    # send a request to join a schedule ride
    url(
        regex=r'^addreq/$',
        view=AddRequestScheduleRide.as_view(),
        name='add_request'
    ),

    # list the requests i made
    url(
        regex=r'^reqimade/$',
        view=ListRequestsIMade.as_view(),
        name='requests_i_made'
    ),

    # list the requests sent to my schedule rides
    url(
        regex=r'^reqtome/$',
        view=ListRequestsToMe.as_view(),
        name='requests_to_me'
    ),

    # accept a request
    url(
        regex=r'^acceptreq/(?P<pk>[0-9]+)/$',
        view=AcceptRequestAPIView.as_view(),
        name='accept_request'
    ),

    # ignore a request
    url(
        regex=r'^ignorereq/(?P<pk>[0-9]+)/$',
        view=IgnoreRequestAPIView.as_view(),
        name='ignore_request'
    ),

    # cancel request i made
    url(
        regex=r'^cancelreq/(?P<pk>[0-9]+)/$',
        view=CancelReqIMade.as_view(),
        name='cancel_request'
    ),

    # list all joined bikers to my schedule ride
    url(
        regex=r'^joined/(?P<pk>[0-9]+)/$',
        view=CheckJoinedBikers.as_view(),
        name='joined_bikers'
    ),

    # cancel joining a schedule ride after my request have approved.
    url(
        regex=r'^canceljoining/(?P<pk>[0-9]+)/$',
        view=CancelJoiningScheduleRide.as_view(),
        name='cancel_joining'
    ),
]
