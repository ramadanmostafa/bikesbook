from django.conf.urls import url
from .views import ScheduleRideList, AddNewScheduleRideCreateAPIView, UpdateMyScheduleRideAPIView,\
    DeleteMyScheduleRideDestroyAPIView, ScheduleRidesNearMeListAPIView, AddRequestScheduleRide, ListRequestsIMade,\
    ListRequestsToMe, AcceptRequestAPIView, IgnoreRequestAPIView, CancelReqIMade, CheckJoinedBikers


urlpatterns = [
    url(r'^$', ScheduleRideList.as_view(), name='list_my_schedule_rides'),
    url(r'^addnewscheduleride/$', AddNewScheduleRideCreateAPIView.as_view(), name='add_new_schedule_ride'),
    url(r'^deletescheduleride/(?P<pk>[0-9]+)/$', DeleteMyScheduleRideDestroyAPIView.as_view(), name='delete_schedule_ride'),
    url(r'^updatescheduleride/(?P<pk>[0-9]+)/$', UpdateMyScheduleRideAPIView.as_view(), name='update_schedule_ride'),
    url(r'^ridesnearme/(?P<city>[0-9a-zA-Z]+)/$', ScheduleRidesNearMeListAPIView.as_view(), name='rides_near_me'),
    url(r'^addreq/$', AddRequestScheduleRide.as_view(), name='add_request'),
    url(r'^reqimade/$', ListRequestsIMade.as_view(), name='requests_i_made'),
    url(r'^reqtome/$', ListRequestsToMe.as_view(), name='requests_to_me'),

    url(r'^acceptreq/(?P<pk>[0-9]+)/$', AcceptRequestAPIView.as_view(), name='accept_request'),
    url(r'^ignorereq/(?P<pk>[0-9]+)/$', IgnoreRequestAPIView.as_view(), name='ignore_request'),
    url(r'^cancelreq/(?P<pk>[0-9]+)/$', CancelReqIMade.as_view(), name='cancel_request'),
    url(r'^joined/(?P<pk>[0-9]+)/$', CheckJoinedBikers.as_view(), name='joined_bikers'),
]