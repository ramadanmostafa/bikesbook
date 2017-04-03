import re
from custom_user.forms import SetPasswordForm

from custom_user.models import CustomUser, EmailConfirmed
from custom_user.utils import send_sms, _get_pin
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.settings import api_settings
from serializers import UserCreateSerializer, UserDetailSerializer, FbUserSerializer, TwitterUserSerializer, \
    AvatarSerializer, ResetPassSerializer, ChangePasswordSerializer, chkactivationSerializer, reactivationSerializer, \
    checkmobindbSerializer, SettingsSerializer, UploadFileSerializer
from .permissions import IsOwner

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserList(ListAPIView):
    '''
    Retutn List of system users this option is available only for admin staff
    '''
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsAdminUser,)


class UserDetailAPIView(RetrieveAPIView):
    '''
    For authenticated users only
    Returns a JSON object with id,username,email,avatar,first_name,last_name and country_code
    '''
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwner]


    def get_object(self):
        header_token = self.request.META.get('HTTP_AUTHORIZATION')
        # token = self.request.query_params.get('jwt')
        if header_token:
            token = header_token.split(' ')[1]
            payload = jwt_decode_handler(token)
            obj = CustomUser.objects.get(id=payload['user_id'])
            return obj


class UserUpdateAPIView(RetrieveUpdateAPIView):
    '''
        For authenticated users only in case user wants to update his information
        Returns a JSON object with updated
        id,username,email,avatar,first_name,last_name and country_code
    '''
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwner]

    def update(self, request, *args, **kwargs):
        return super(UserUpdateAPIView, self).update(request, *args, partial=True)

    def get_object(self):
        header_token = self.request.META.get('HTTP_AUTHORIZATION')
        # token = self.request.query_params.get('jwt')
        if header_token:
            token = header_token.split(' ')[1]
            payload = jwt_decode_handler(token)
            obj = CustomUser.objects.get(id=payload['user_id'])
            return obj

class SettingUpdateAPIView(RetrieveUpdateAPIView):
    '''
            SettingUpdateAPIView
    '''
    queryset = CustomUser.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsOwner]

    def update(self, request, *args, **kwargs):
        return super(SettingUpdateAPIView, self).update(request, *args, partial=True)

    def get_object(self):
        header_token = self.request.META.get('HTTP_AUTHORIZATION')
        # token = self.request.query_params.get('jwt')
        if header_token:
            token = header_token.split(' ')[1]
            payload = jwt_decode_handler(token)
            obj = CustomUser.objects.get(id=payload['user_id'])
            return obj.setting


class ChangePassword(RetrieveUpdateAPIView):
    '''
     change password for authenticated users
    '''
    serializer_class = ChangePasswordSerializer

    def put(self, request, *args, **kwargs):
        data = self.request.data
        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            if self.request.user.check_password(serializer.data['old_password']):
                if serializer.data['new_password'] == serializer.data['new_password2']:
                    self.request.user.set_password(serializer.data['new_password'])
                    self.request.user.save()
                    return Response({"success": "Password has been reset."}, status=HTTP_200_OK)
            else:
                return Response({"error": "wrong password"}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


class UserCreateAPIView(CreateAPIView):
    """
        API View that receives a POST with a user's
        full_name , username, password, avatar , email and country_code \n
        send an email to this user \n
        Returns success message if this user has been successfully created \n
        IOError : {"code": "IOError"} IOError During send message \n
        1 : Success \n
        -1 : Validation Error  \n
        1 : Confirmation message has been sent please check you message.
    """
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'code': 1},status=HTTP_200_OK)
        return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


class FbCreateAPIView(CreateAPIView):
    '''
    For Facebook users
    API View that receives a POST with a user's fb_access_tokens , fb_id
    Returns a JSON Web Token that can be used for authenticated requests.
    '''
    serializer_class = FbUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = FbUserSerializer(data=data)
        if serializer.is_valid():
            our_user = serializer.save()
            payload = jwt_payload_handler(our_user)
            return Response({'token': jwt_encode_handler(payload)}, status=HTTP_200_OK)
        return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


class TwitterCreateAPIView(CreateAPIView):
    '''
    For Twitter users
    API View that receives a POST with a user's TWITTER_OAUTH_TOKEN , TWITTER_OAUTH_TOKEN_SECRET and twitter_id
    Returns a JSON Web Token that can be used for authenticated requests.
    '''
    serializer_class = TwitterUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TwitterUserSerializer(data=data)
        if serializer.is_valid():
            our_user = serializer.save()
            payload = jwt_payload_handler(our_user)
            return Response({'token': jwt_encode_handler(payload)}, status=HTTP_200_OK)
        return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


class UploadAvatar(APIView):
    '''
     For authenticated users only in case user want to change his avatar
     Returns HTTP status=201 created
    '''
    serializer_class = AvatarSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = AvatarSerializer(data=data)
        if serializer.is_valid():
            avatar = request.FILES['avatar']
            header_token = self.request.META.get('HTTP_AUTHORIZATION')
            if header_token:
                token = header_token.split(' ')[1]
                payload = jwt_decode_handler(token)
                user = CustomUser.objects.get(id=payload['user_id'])
                if user.avatar:
                    user.avatar.delete()
                user.avatar = avatar
                user.save()
                return Response({}, status=201)
        else:
            return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


from django.core.files.storage import FileSystemStorage
import os
class UploadRide(APIView):
    '''
     For authenticated users only in case user want to upload his ride
     Returns HTTP status=201 created
    '''
    serializer_class = UploadFileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UploadFileSerializer(data=data)
        if serializer.is_valid():
            upload = request.FILES['ridefile']
            header_token = self.request.META.get('HTTP_AUTHORIZATION')
            if header_token:
                token = header_token.split(' ')[1]
                payload = jwt_decode_handler(token)
                user = CustomUser.objects.get(id=payload['user_id'])
                fs = FileSystemStorage()
                directory = os.path.dirname(fs.location+"/"+user.mobile_number+"/")
                fs = FileSystemStorage(location=directory)
                if not os.path.exists(directory):
                        os.makedirs(directory)
                filename = fs.save(upload.name, upload)
                uploaded_file_url = "%s%s%s/%s" % (settings.SITE_URL,fs.base_url,user.mobile_number,filename)
                return Response({"uploaded_file_url":uploaded_file_url}, status=201)
        else:
            return Response({'code': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class ForgetPassword(APIView):
    '''
        send ChangePassword mail to user then he can login with his new password
    '''

    serializer_class = ResetPassSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ResetPassSerializer(data=data)
        if serializer.is_valid():
            associated_user = CustomUser.objects.get(email=serializer.data['email'])
        if not associated_user.is_social:
            payload = jwt_payload_handler(associated_user)
            token = jwt_encode_handler(payload)
            # token = self.request.user.auth_token.key
            uid = urlsafe_base64_encode(force_bytes(associated_user.pk))
            reset_pass_url = "%s%s" % (settings.SITE_URL, reverse("reset_password_confirm", args=[uid, token]))
            context = {
                "reset_url": reset_pass_url,
                "user": associated_user.username,
            }
            message = render_to_string("accounts/reset_message.txt", context)
            subject = "Reset Your password"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [associated_user.email], fail_silently=True)
            return Response({'code': ' Reset password mail has been sent please check you mail.'},
                            status=HTTP_200_OK)
        else:
            return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(FormView):
    template_name = "accounts/reset_password.html"
    success_url = '/'
    form_class = SetPasswordForm

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """
        UserModel = get_user_model()
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None
        payload = jwt_decode_handler(token)
        if user is not None and (user.id == payload['user_id']):
            if form.is_valid():
                new_password = form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset.')
                return self.form_valid(form)
            else:
                messages.error(request, 'Password reset has not been unsuccessful.', 'danger')
                return self.form_invalid(form)
        else:
            messages.error(request, 'The reset password link is no longer valid.')
            return self.form_invalid(form)


SHA1_RE = re.compile('^[a-f0-9]{40}$')


def activation_view(request, activation_key):
    if SHA1_RE.search(activation_key):
        print "activation key is real"
        try:
            instance = EmailConfirmed.objects.get(activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            messages.error(request, "There was an error with your request.", 'danger')
        if instance is not None and not instance.confirmed:
            instance.confirmed = True
            instance.user.is_active = True
            instance.user.save()
            instance.save()
            messages.success(request, "Successfully Confirmed! Please login.")
        elif instance is not None and instance.confirmed:
            messages.warning(request, "Already Confirmed.")
        else:
            pass
        return HttpResponseRedirect("/")
    else:
        raise Http404


class chkactivation(APIView):
    '''
        check if user has enter correct value for pin code and return token if valid \n
        -1 : {'code': -1}  Validation Error \n
        0 : {'code': 0}  Incorrect Pin Code \n
    '''

    serializer_class = chkactivationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = chkactivationSerializer(data=data)
        if serializer.is_valid():
            associated_user = CustomUser.objects.get(mobile_number=serializer.data['mobile_number'])
            if associated_user.pin_code == serializer.data['pin_code']:
                associated_user.is_active = True
                associated_user.save()
                payload = jwt_payload_handler(associated_user)
                return Response({'token': jwt_encode_handler(payload)}, status=HTTP_200_OK)
            else:
                return Response({'code': 0}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


class reactivation(APIView):
    '''
        resend activiation code

        IOError : {"message": "IOError"}  IOError During send message \n
        1 : {'code':  1}   Confirmation message has been sent please check you message. \n
       -1 : {'code': -1}  Validation Error \n
    '''

    serializer_class = reactivationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = reactivationSerializer(data=data)
        if serializer.is_valid():
            mobile_number = serializer.data['mobile_number']
            associated_user = CustomUser.objects.get(mobile_number=serializer.data['mobile_number'])
            pin_code = _get_pin(length=4)
            associated_user.pin_code = pin_code
            associated_user.save()
            send_sms_data = 'Username={0}&Password={1}&Sender=BikesBook&Recipients={2}&MessageData=Activation Code: {3}'.format(
                    'IntelliCoders', 'Intellicaders17', mobile_number, pin_code)
            send_sms(send_sms_url='http://tekegy.org/?', send_sms_data=send_sms_data)

            return Response({'code': 1},status=HTTP_200_OK)
        else:
            return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)


class checkmobindb(APIView):
    '''
        check if mobile number exists on data base or not
        if exists it send sms to this number \n

         IOError : {"code": "IOError"}  IOError During send message
         1 : Success \n
        -1 : Validation Error \n
        0:Your mobile number is already registered \n
        2:Your mobile number is not registered \n
    '''

    serializer_class = checkmobindbSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = checkmobindbSerializer(data=data)
        if serializer.is_valid():
            mobile_number = serializer.data['mobile_number']
            try:
                associated_user = CustomUser.objects.get(mobile_number=serializer.data['mobile_number'])
                if associated_user and serializer.data['signup'] ==True:return Response({'code': 0}, status=HTTP_400_BAD_REQUEST)
            except CustomUser.DoesNotExist:
                return Response({'code': 2}, status=HTTP_400_BAD_REQUEST)
            else:
                pin_code = _get_pin(length=4)
                associated_user.pin_code = pin_code
                associated_user.save()
                send_sms_data = 'Username={0}&Password={1}&Sender=BikesBook&Recipients={2}&MessageData=Activation Code: {3}'.format(
                        'IntelliCoders', 'Intellicaders17', mobile_number, pin_code)
                send_sms(send_sms_url='http://tekegy.org/?', send_sms_data=send_sms_data)

                return Response({'code': 1},
                                status=HTTP_200_OK)
        else:
            return Response({'code': -1}, status=HTTP_400_BAD_REQUEST)
