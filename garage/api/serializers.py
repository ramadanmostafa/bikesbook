from custom_user.api.serializers import UserDetailSerializer
from garage.models import (Garage, BicycleMake, BicyceStyle, Motorcycle,
                           Bicycle, NewMotorcycle, MotorModel, MotorMake, MotorStyle, MotorEngine, NewBicycle, Motorcycle)
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer


class BicyceSerializer(ModelSerializer):
    class Meta:
        model = Bicycle
        fields = [
            'id',
            'make',
            'style',
            'color',
            'default'
        ]
        extra_kwargs = {"id": {"read_only": True}}




# class RideSerializer(ModelSerializer):
#     class Meta:
#         model = Ride
#         fields = [
#             'id',
#             'start_lat',
#             'start_lng',
#             'end_lat',
#             'end_lng',
#             'distance',
#             'duration',
#             'max_speed',
#             'start_time',
#             'end_time',
#             'bicycle',
#             'motorcycle',
#             "path_file"
#         ]
#         extra_kwargs = {"id": {"read_only": True}}

class BicycemsSerializer(ModelSerializer):
    class Meta:
        model = NewBicycle
        fields = [
            'make',
            'style',
        ]


class BicyceListSerializer(ModelSerializer):
    make = serializers.CharField(source='make.brand', read_only=True)
    make_id = serializers.IntegerField(source='make.id', read_only=True)
    style = serializers.CharField(source='style.style', read_only=True)
    style_id = serializers.IntegerField(source='style.id', read_only=True)

    class Meta:
        model = Bicycle
        fields = [
            'id',
            'make',
            'make_id',
            'style',
            'style_id',
            'color',
            'default'
        ]
        extra_kwargs = {"id": {"read_only": True}}


class MotorSerializer(ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = [
            'id',
            'make',
            'model',
            'style',
            'engine_size',
            'production_year',
            'color',
            'default'
        ]


class MotorListSerializer(ModelSerializer):
    make = serializers.CharField(source='make.brand', read_only=True)
    make_id = serializers.IntegerField(source='make.id', read_only=True)
    model = serializers.CharField(source='model.model', read_only=True)
    model_id = serializers.IntegerField(source='model.id', read_only=True)
    style = serializers.CharField(source='style.style', read_only=True)
    style_id = serializers.IntegerField(source='style.id', read_only=True)
    engine_size = serializers.CharField(source='engine_size.cc', read_only=True)
    engine_size_id = serializers.IntegerField(source='engine_size.id', read_only=True)

    class Meta:
        model = Motorcycle
        fields = [
            'id',
            'make',
            'make_id',
            'model',
            'model_id',
            'style',
            'style_id',
            'engine_size',
            'engine_size_id',
            'production_year',
            'color',
            'default'
        ]

    extra_kwargs = {"id": {"read_only": True}}


class GarageCreateSerializer(ModelSerializer):
    class Meta:
        model = Garage
        fields = ('name',)


class GarageDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    bicycles = BicyceListSerializer(read_only=True, many=True)
    motorcycles = MotorListSerializer(read_only=True, many=True)

    class Meta:
        model = Garage
        fields = [
            'id',
            'user',
            'bicycles',
            'motorcycles',
        ]

        # def get_bicycles(self, obj):
        #     c_qs = obj.bicycles.get_queryset()
        #     bicycles = BicyceSerializer(c_qs, many=True).data
        #     return bicycles
        #
        # def get_motorcycles(self, obj):
        #     c_qs = obj.motorcycles.get_queryset()
        #     motorcycles = MotorSerializer(c_qs, many=True).data
        #     return motorcycles


class BicycleMakeSerializer(ModelSerializer):
    class Meta:
        model = BicycleMake
        fields = [
            'id',
            'brand',
        ]


class MotorModelSerializer(ModelSerializer):
    class Meta:
        model = MotorModel
        fields = [
            'id',
            'model',
        ]


class SpeMotorMakeSerializer(ModelSerializer):
    models = SerializerMethodField()

    class Meta:
        model = MotorMake
        fields = [
            'id',
            'brand',
            'models'
        ]

    def get_models(self, obj):
        c_qs = MotorModel.objects.filter(make=obj)
        models = MotorModelSerializer(c_qs, many=True).data
        return models


class MotorMakeSerializer(ModelSerializer):
    class Meta:
        model = MotorMake
        fields = [
            'id',
            'brand',
        ]


class BicyceStyleSerializer(ModelSerializer):
    class Meta:
        model = BicyceStyle
        fields = [
            'id',
            'style',
        ]


class MotorStyleSerializer(ModelSerializer):
    class Meta:
        model = MotorStyle
        fields = [
            'id',
            'style',
        ]


class MotorEngineSerializer(ModelSerializer):
    class Meta:
        model = MotorEngine
        fields = [
            'id',
            'cc',
        ]


# class PointListSerializer(ModelSerializer):
#     ride = RideSerializer(read_only=True)
#     class Meta:
#         model = Point
#         fields = [
#             'id',
#             'ride',
#             'lat',
#             'lng',
#         ]

class BicycleNewSerializer(ModelSerializer):
    class Meta:
        model = NewBicycle
        fields = [
            "make",
            "style"
        ]
class MotorcycleNewSerializer(ModelSerializer):
    class Meta:
        model = NewMotorcycle
        fields = [
            "make",
            "style",
            "engine_size",
            "model"
        ]