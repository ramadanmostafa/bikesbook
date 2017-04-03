from custom_user.utils import _get_pin, send_sms
from django.contrib.auth.backends import ModelBackend
from models import CustomUser


class CustomUserAuth(ModelBackend):
    # keyword -args should be username and password to be able to login with django admin
    def authenticate(self, username=None, mobile_number=None, password=None):
        try:
            # user = CustomUser.objects.get(email=username or mobile_number)
            user = CustomUser.objects.get(mobile_number=username or mobile_number)
            if not user.is_staff:
                user.pin_code = _get_pin(length=4)
                user.is_active = False
                user.save()  # fire user create signal
                send_sms_data = 'Username={0}&Password={1}&Sender=BikesBook&Recipients={2}&MessageData=Activation Code: {3}'.format(
                        'IntelliCoders', 'Intellicaders17', user.mobile_number, user.pin_code)
                send_sms(send_sms_url='http://tekegy.org/?', send_sms_data=send_sms_data)
            if user:
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None