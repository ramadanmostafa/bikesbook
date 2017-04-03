from custom_user.models import CustomUser
from garage.api.permissions import IsOwner, IsGarageOwner, IsBicycleOwner, IsMotorcycleOwner, IsbikeOwner
from garage.models import (Garage, BicycleMake, BicyceStyle, Motorcycle, NewMotorcycle, NewBicycle,
                           Bicycle, MotorMake, MotorModel, MotorStyle, MotorEngine)
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_jwt.utils import jwt_decode_handler
from serializers import (GarageDetailSerializer, BicycleMakeSerializer,
                         BicyceStyleSerializer, BicyceSerializer, MotorSerializer, MotorMakeSerializer,
                         MotorModelSerializer, SpeMotorMakeSerializer, MotorStyleSerializer, MotorEngineSerializer,
                         BicyceListSerializer, MotorListSerializer, BicycemsSerializer,
                         BicycleNewSerializer, MotorcycleNewSerializer)


class GarageDetailAPIView(RetrieveAPIView):
    '''
        Retutn Json object contains all user garage details bicycles,motorcycles,...etc
    '''
    serializer_class = GarageDetailSerializer
    permission_classes = [IsOwner]

    def get_object(self):
        header_token = self.request.META.get('HTTP_AUTHORIZATION')
        if header_token:
            token = header_token.split(' ')[1]
            payload = jwt_decode_handler(token)
            current_user = CustomUser.objects.get(id=payload['user_id'])
            current_garage = Garage.objects.get(user=current_user)
            return current_garage


class BicycleMakeListAPIView(ListAPIView):
    '''
        Retutn list of available Bicycle Makes
    '''
    serializer_class = BicycleMakeSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        # ./manage.py sqlsequencereset garage
        return BicycleMake.objects.filter(active=True)


class MotorMakeListAPIView(ListAPIView):
    '''
        Retutn list of available Motorcycle Makes
    '''
    queryset = MotorMake.objects.all()
    serializer_class = MotorMakeSerializer
    permission_classes = [AllowAny, ]


class SpeMotorMakeListAPIView(RetrieveAPIView):
    '''
     list of available models for selected motor make
    '''
    queryset = MotorMake.objects.all()
    serializer_class = SpeMotorMakeSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'


class MotorModelListAPIView(RetrieveAPIView):
    queryset = MotorModel.objects.all()
    serializer_class = MotorModelSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'


class BicycleStyleListAPIView(ListAPIView):
    '''
        Retutn list of available Bicycle styles
    '''

    serializer_class = BicyceStyleSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return BicyceStyle.objects.filter(active=True)


class MotorStyleListAPIView(ListAPIView):
    '''
     return list of motorcycle styles
    '''
    queryset = MotorStyle.objects.all()
    serializer_class = MotorStyleSerializer
    permission_classes = [AllowAny, ]


class MotorCCListAPIView(ListAPIView):
    '''
     list of Motor CC
    '''
    queryset = MotorEngine.objects.all()
    serializer_class = MotorEngineSerializer
    permission_classes = [AllowAny, ]


class BicycleCreateAPIView(CreateAPIView):
    '''
      add new Bicycle to user garage required fields are Make and Style ids
    '''
    serializer_class = BicyceSerializer
    permission_classes = [IsGarageOwner, ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            user_bicycle = Bicycle(**serializer.validated_data)
            if serializer.data['default']:
                Motorcycle.objects.update(default=False)
                Bicycle.objects.update(default=False)
            user_bicycle.save()
            user_garage = Garage.objects.get(user=self.request.user)
            user_bicycle.garage_set.add(user_garage)


# class RideCreateAPIView(CreateAPIView):
#     '''
#       add new Ride to user
#     '''
#     serializer_class = RideSerializer
#     permission_classes = [IsGarageOwner,IsbikeOwner]
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=self.request.data)
#         if serializer.is_valid():
#             user = self.request.user
#             new_ride = Ride(user=user, **serializer.validated_data)
#             new_ride.save()
#             return Response({'ride_id': new_ride.id}, status=HTTP_200_OK)
#         else:
#             return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)




class BicyclemsCreateAPIView(CreateAPIView):
    '''
      add new make and style to bicycle list
    '''
    serializer_class = BicycemsSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            make = serializer.data['make']
            style = serializer.data['style']
            new_style = BicyceStyle(style=style, active=False)
            new_style.save()
            new_make = BicycleMake(brand=make, active=False)
            new_make.save()
            return Response({'code': 1}, status=HTTP_200_OK)
        else:
            return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


class MotorCreateAPIView(CreateAPIView):
    '''
     add new Motor cycle to user garage
    '''
    serializer_class = MotorSerializer
    permission_classes = [IsGarageOwner, ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            user_motorcycle = Motorcycle(**serializer.validated_data)
            if serializer.data['default']:
                Motorcycle.objects.update(default=False)
                Bicycle.objects.update(default=False)
            user_motorcycle.save()
            user_garage = Garage.objects.get(user=self.request.user)
            user_motorcycle.garage_set.add(user_garage)


class BicycleListAPIView(ListAPIView):
    '''
     list of current user Bicycles
    '''
    serializer_class = BicyceListSerializer
    permission_classes = [IsBicycleOwner]

    def get_queryset(self, *args, **kwargs):
        garage = Garage.objects.get(user=self.request.user)
        queryset_list = garage.bicycles.all()
        return queryset_list


class UpdateBicycleAPIView(RetrieveUpdateAPIView):
    '''
        update Bicycle data for current user
    '''
    queryset = Bicycle.objects.all()
    serializer_class = BicyceSerializer
    permission_classes = [IsBicycleOwner]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        if request.data['default']:
            Motorcycle.objects.update(default=False)
            Bicycle.objects.update(default=False)
        return super(UpdateBicycleAPIView, self).update(request, *args, partial=True)


class DeleteBicycleAPIView(DestroyAPIView):
    '''
        Delete Bicycle from current user garage
    '''
    queryset = Bicycle.objects.all()
    serializer_class = BicyceSerializer
    permission_classes = [IsBicycleOwner]
    lookup_field = 'pk'


class UpdateMotorcycleAPIView(RetrieveUpdateAPIView):
    '''
        update Motorcycle data for current user
    '''
    queryset = Motorcycle.objects.all()
    serializer_class = MotorSerializer
    permission_classes = [IsMotorcycleOwner]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        if request.data['default']:
            Motorcycle.objects.update(default=False)
            Bicycle.objects.update(default=False)
        return super(UpdateMotorcycleAPIView, self).update(request, *args, partial=True)


class DeleteMotorcycleAPIView(DestroyAPIView):
    '''
     delete motorcycle from current user garage
    '''
    queryset = Motorcycle.objects.all()
    serializer_class = MotorSerializer
    permission_classes = [IsMotorcycleOwner]
    lookup_field = 'pk'


class MotorcycleListAPIView(ListAPIView):
    '''
     list of current user Motorcycles
    '''
    serializer_class = MotorListSerializer
    permission_classes = [IsMotorcycleOwner]

    def get_queryset(self, *args, **kwargs):
        garage = Garage.objects.get(user=self.request.user)
        queryset_list = garage.motorcycles.all()
        return queryset_list





class AddNewBikeAPIView(CreateAPIView):
    '''
    add new bike to the pending table, then will be added to the database if confirmed from the admin page
    '''
    serializer_class = BicycleNewSerializer
    permission_classes = []

    def perform_create(self, serializer):
        if serializer.is_valid():
            new_bike = NewBicycle(**serializer.validated_data)
            new_bike.save()

class AddNewMotorcycleAPIView(CreateAPIView):
    '''
    add new Motorcycle to the pending table, then will be added to the database if confirmed from the admin page
    '''
    serializer_class = MotorcycleNewSerializer
    permission_classes = []

    def perform_create(self, serializer):
        if serializer.is_valid():
            new_motor = NewMotorcycle(**serializer.validated_data)
            new_motor.save()