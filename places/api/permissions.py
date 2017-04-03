from rest_framework.permissions import BasePermission
from custom_user.models import CustomUser
from rest_framework_jwt.utils import jwt_decode_handler


class IsAuthenticated(BasePermission):

    message = 'You must be the owner of this object.'

    def has_permission(self, request, view):

        header_token = request.META.get('HTTP_AUTHORIZATION')
        if header_token:
            token = header_token.split(' ')[1]
            payload = jwt_decode_handler(token)
            obj = CustomUser.objects.get(id=payload['user_id'])
            return obj == request.user

class IsOwner(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user