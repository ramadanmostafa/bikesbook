from custom_user.models import CustomUser
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework_jwt.utils import jwt_decode_handler
from garage.models import Garage,Bicycle,Motorcycle


class IsOwner(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsGarageOwner(BasePermission):
    message = 'You must be the owner of Garage object.'

    def has_permission(self, request, view):
        header_token = request.META.get('HTTP_AUTHORIZATION')
        # token = self.request.query_params.get('jwt')
        if header_token:
            token = header_token.split(' ')[1]
            payload = jwt_decode_handler(token)
            obj = CustomUser.objects.get(id=payload['user_id'])
            garage = Garage.objects.get(user=obj)
            return garage.user == request.user

class IsbikeOwner(BasePermission):
    message = 'You must be the owner of bike object.'

    def has_permission(self, request, view):
            if request.data.has_key('bicycle'):
                return Bicycle.objects.filter(id=int(request.data['bicycle'])).exists()
            elif request.data.has_key('motorcycle'):
                return Motorcycle.objects.filter(id=int(request.data['motorcycle'])).exists()
            else:
                return False


class IsBicycleOwner(BasePermission):
    message = 'You must be the owner of this Bicycle.'

    def has_object_permission(self, request, view, obj):
        garage = Garage.objects.get(user=request.user)
        return obj in garage.bicycles.all()


class IsMotorcycleOwner(BasePermission):
    message = 'You must be the owner of this Motorcycle'

    def has_object_permission(self, request, view, obj):
        garage = Garage.objects.get(user=request.user)
        return obj in garage.motorcycles.all()
