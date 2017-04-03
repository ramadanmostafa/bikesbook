"""bikesbook URL Configuration
"""
from django.conf.urls import url
from garage.api.views import (GarageDetailAPIView, BicycleMakeListAPIView,BicyclemsCreateAPIView,
                              BicycleStyleListAPIView, BicycleCreateAPIView, MotorCreateAPIView, MotorMakeListAPIView,
                              MotorModelListAPIView, SpeMotorMakeListAPIView, MotorStyleListAPIView, MotorCCListAPIView,
                              UpdateBicycleAPIView, UpdateMotorcycleAPIView, DeleteMotorcycleAPIView, AddNewBikeAPIView,
                              DeleteBicycleAPIView,BicycleListAPIView,MotorcycleListAPIView, AddNewMotorcycleAPIView)

urlpatterns = [
    url(r'^detail/$', GarageDetailAPIView.as_view(), name='detail'),
    url(r'^bicyclemakes/$', BicycleMakeListAPIView.as_view(), name='bicyclemakes'),
    url(r'^bicyclestyles/$', BicycleStyleListAPIView.as_view(), name='bicyclestyles'),
    url(r'^addbicycle/$', BicycleCreateAPIView.as_view(), name='addbicycle'),
    url(r'^addbicyclems/$', BicyclemsCreateAPIView.as_view(), name='addbicyclems'),
    url(r'^bicyclelist/$', BicycleListAPIView.as_view(), name='bicyclelist'),
    url(r'^updatebicycle/(?P<pk>[0-9]+)/$', UpdateBicycleAPIView.as_view(), name='updatebicycle'),
    url(r'^delbicycle/(?P<pk>[0-9]+)/$', DeleteBicycleAPIView.as_view(), name='delbicycle'),
    url(r'^motormakes/$', MotorMakeListAPIView.as_view(), name='motormakes'),
    url(r'^motormakes/(?P<pk>[0-9]+)/$', SpeMotorMakeListAPIView.as_view(), name='spe_motormakes'),
    # url(r'^motormodels/(?P<pk>[0-9]+)/$', MotorModelListAPIView.as_view(), name='motormodels'),
    url(r'^motorstyles/$', MotorStyleListAPIView.as_view(), name='motorstyles'),
    url(r'^motorcc/$', MotorCCListAPIView.as_view(), name='motorcc'),
    url(r'^addmotorcycle/$', MotorCreateAPIView.as_view(), name='addmotorcycle'),
    url(r'^motorcyclelist/$', MotorcycleListAPIView.as_view(), name='motorcyclelist'),
    url(r'^updatemotorcycle/(?P<pk>[0-9]+)/$', UpdateMotorcycleAPIView.as_view(), name='updatemotorcycle'),
    url(r'^delmotorcycle/(?P<pk>[0-9]+)/$', DeleteMotorcycleAPIView.as_view(), name='delmotorcycle'),

    # add a new bicycle style, make
    url(r'^addnewbike/$', AddNewBikeAPIView.as_view(), name="add_new_bike"),

    # add a new motorcycle style, make, engine size, model
    url(r'^addnewmotorcycle/$', AddNewMotorcycleAPIView.as_view(), name="add_new_motorcycle"),


    # url(r'^addpoint/$', PointCreateAPIView.as_view(), name='addpoint'),
    # url(r'^pointlist/(?P<pk>[0-9]+)/$', PointListAPIView.as_view(), name='pointlist'),
    # url(r'^ridelist/$', RideListAPIView.as_view(), name='ridelist'),
]
