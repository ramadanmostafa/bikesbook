from .views import RideStartAPIView, RideEndAPIView, RideFileAPIView, RideListAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^startride/$', RideStartAPIView.as_view(), name='startride'),
    url(r'^endride/$', RideEndAPIView.as_view(), name='endride'),
    url(r'^ridefile/$', RideFileAPIView.as_view(), name='ridefile'),
    url(r'^listrides/$', RideListAPIView.as_view(), name='listrides'),
]