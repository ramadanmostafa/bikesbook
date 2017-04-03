from django.conf.urls import url
from .views import MyPlacesListAPIView, AddNewPlaceCreateAPIView, DeleteMyPlaceDestroyAPIView, UpdateMyPlaceAPIView

urlpatterns = [
    url(r'^$', MyPlacesListAPIView.as_view(), name='list_myplaces'),
    url(r'^addnewplace/$', AddNewPlaceCreateAPIView.as_view(), name='addnewplace'),
    url(r'^deleteplace/(?P<pk>[0-9]+)/$', DeleteMyPlaceDestroyAPIView.as_view(), name='deleteplace'),
    url(r'^updateplace/(?P<pk>[0-9]+)/$', UpdateMyPlaceAPIView.as_view(), name='updateplace'),
    ]