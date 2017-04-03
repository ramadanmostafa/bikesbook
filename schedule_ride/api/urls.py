from django.conf.urls import url
from .views import ScheduleRideListAPIView, AddNewScheduleRideCreateAPIView, UpdateMyScheduleRideAPIView,\
    DeleteMyScheduleRideDestroyAPIView, ScheduleRidesNearMeListAPIView, AddRequestScheduleRide, ListRequestsIMade


urlpatterns = [
    url(r'^$', ScheduleRideListAPIView.as_view(), name='list_my_schedule_rides'),
    url(r'^addnewscheduleride/$', AddNewScheduleRideCreateAPIView.as_view(), name='add_new_schedule_ride'),
    url(r'^deletescheduleride/(?P<pk>[0-9]+)/$', DeleteMyScheduleRideDestroyAPIView.as_view(), name='delete_schedule_ride'),
    url(r'^updatescheduleride/(?P<pk>[0-9]+)/$', UpdateMyScheduleRideAPIView.as_view(), name='update_schedule_ride'),
    url(r'^ridesnearme/(?P<city>[0-9a-zA-Z]+)/$', ScheduleRidesNearMeListAPIView.as_view(), name='rides_near_me'),
    url(r'^addreq/$', AddRequestScheduleRide.as_view(), name='add_request'),
    url(r'^reqimade/$', ListRequestsIMade.as_view(), name='requests_i_made'),
    ]