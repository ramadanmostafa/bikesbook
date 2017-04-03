from urllib2 import urlopen, HTTPError

import oauth2
from custom_user.models import CustomUser,Setting
from custom_user.utils import _get_pin, send_sms
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ImageField, EmailField, IntegerField,BooleanField,DateField,FileField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from simplejson import loads
from django.conf import settings


class UserCreateSerializer(ModelSerializer):
    # username = CharField()
    # email = EmailField(label='Email Address')
    #password = CharField(label='Enter Password', required=True)

    class Meta:
        model = CustomUser
        fields = ('country_code','mobile_number','full_name')
        #extra_kwargs = {"password": {"write_only": True}}

    # def validate(self, data):
    #     email = data['email']
    #     username = data['username']
    #     user_qs = CustomUser.objects.filter(Q(email=email) | Q(username=username))
    #     if user_qs.exists():
    #         raise ValidationError("This user has already registered.")
    #     return data

    def create(self, validated_data):
        #validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser(**validated_data)
        if not user.avatar:
            user.avatar = '/static/img/placeholder.png'
        add_membership_id(user)
        user.pin_code = _get_pin(length=4)
        user.save()  # fire user create signal
        send_sms_data = 'Username={0}&Password={1}&Sender=BikesBook&Recipients={2}&MessageData=Activation Code: {3}'.format(
                'IntelliCoders', 'Intellicaders17', user.mobile_number, user.pin_code)
        send_sms(send_sms_url='http://tekegy.org/?', send_sms_data=send_sms_data)

        # try:
        #     content = loads(urlopen(url).read())
        # except HTTPError:
        #     raise ValidationError("Error sending sms please try again")
        return user

class SettingsSerializer(ModelSerializer):

    class Meta:
        model = Setting
        fields = [
            'id',
            'Allow_bikers_join',
            'get_sos_notifications',
            'gps_acc',
            'distance_unit',
            'connect_with_fb',
            'connect_with_twitter',
            'publish_time_interval',
            'share_my_info_using'

        ]
        extra_kwargs = {"id": {"read_only": True}}


class UserDetailSerializer(ModelSerializer):
    date_of_birth=serializers.DateField(input_formats=['%d/%m/%Y'],format='%d %b %Y')
    setting = SettingsSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'mobile_number',
            'full_name',
            'email',
            'date_of_birth',
            'avatar',
            'country_code',
            'date_joined',
            'setting'
        ]
        extra_kwargs = {"avatar": {"read_only": True}}


class FbUserSerializer(ModelSerializer):
    fb_access_tokens = CharField(max_length=400)
    fb_id = CharField(max_length=400)

    class Meta:
        model = CustomUser
        fields = ('fb_access_tokens', 'fb_id')

    def create(self, validated_data):
        url = 'https://graph.facebook.com/v2.7/me?access_token=%s&fields=id,name,email' % (
            validated_data['fb_access_tokens'],)
        try:
            content = loads(urlopen(url).read())
        except HTTPError:
            raise ValidationError("Signature has been expired.")
        if content['id'] == validated_data['fb_id']:
            if CustomUser.objects.filter(fb_id=validated_data['fb_id']).exists():
                user = CustomUser.objects.get(fb_id=validated_data['fb_id'])
            else:
                generated_password = CustomUser.objects.make_random_password()
                full_name = content['name']
                email = content['email']
                password = make_password(generated_password)
                fb_id = content['id']
                try:
                    user = CustomUser(full_name=full_name, email=email, password=password, fb_id=fb_id, is_social=True,
                                      is_active=True)
                    add_membership_id(user)
                except:
                    raise ValidationError("This user is already registered.")
                user.save()
            return user


def oauth_req(url, key, secret, TWITTER_OAUTH_TOKEN, TWITTER_OAUTH_TOKEN_SECRET, http_method="GET", post_body="",
              http_headers=None):
    consumer = oauth2.Consumer(key=key, secret=secret)
    # TWITTER_OAUTH_TOKEN = "305820916-Q01ESEZ3hledtFITLRGNH2tPC6HKRaOGhJfsQ6lF"
    # TWITTER_OAUTH_TOKEN_SECRET = "kAGWDw2AOXtwRlOC4TgyrZyicKytpF1eH0lCTUKC4DA7x"
    token = oauth2.Token(key=TWITTER_OAUTH_TOKEN, secret=TWITTER_OAUTH_TOKEN_SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


class TwitterUserSerializer(ModelSerializer):
    TWITTER_OAUTH_TOKEN = CharField(max_length=400)
    TWITTER_OAUTH_TOKEN_SECRET = CharField(max_length=400)
    twitter_id = CharField(max_length=400)

    class Meta:
        model = CustomUser
        fields = ('TWITTER_OAUTH_TOKEN', 'TWITTER_OAUTH_TOKEN_SECRET', 'twitter_id')

    def create(self, validated_data):
        try:
            twitter_user_info = oauth_req('https://api.twitter.com/1.1/account/verify_credentials.json',
                                          key=settings.TWITTER_CONSUMER_KEY, secret=settings.TWITTER_CONSUMER_SECRET,
                                          TWITTER_OAUTH_TOKEN=validated_data['TWITTER_OAUTH_TOKEN'],
                                          TWITTER_OAUTH_TOKEN_SECRET=validated_data['TWITTER_OAUTH_TOKEN_SECRET'])
            twitter_user_info = loads(twitter_user_info)
        except HTTPError:
            raise ValidationError("Signature has been expired.")
        if twitter_user_info['id_str'] == validated_data['twitter_id']:
            if CustomUser.objects.filter(twitter_id=validated_data['twitter_id']).exists():
                user = CustomUser.objects.get(twitter_id=validated_data['twitter_id'])
            else:
                generated_password = CustomUser.objects.make_random_password()
                full_name = twitter_user_info['name']
                user_name = twitter_user_info['screen_name']
                email = user_name + "@twitter.com"
                password = make_password(generated_password)
                twitter_id = twitter_user_info['id_str']
                try:
                    user = CustomUser(full_name=full_name, username=user_name, email=email, password=password,
                                      twitter_id=twitter_id, is_social=True, is_active=True)
                except:
                    raise ValidationError("This user is already registered.")
                user.save()
            return user


class AvatarSerializer(serializers.Serializer):
    avatar = ImageField(label='avatar')

class UploadFileSerializer(serializers.Serializer):
    ridefile = FileField(label='ridefile')

class ResetPassSerializer(serializers.Serializer):
    email = EmailField()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = CharField()
    new_password = CharField()
    new_password2 = CharField()


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class chkactivationSerializer(serializers.Serializer):
    pin_code = CharField(max_length=4, validators=[RegexValidator(r'^\d{0,9}$')])
    mobile_number = CharField(validators=[phone_regex], max_length=15)

    class Meta:
        model = CustomUser
        fields = ('pin_code', 'mobile_number')


class reactivationSerializer(serializers.Serializer):
    mobile_number = CharField(validators=[phone_regex], max_length=15)

    class Meta:
        model = CustomUser
        fields = ('mobile_number')


class checkmobindbSerializer(serializers.Serializer):
    mobile_number = CharField(validators=[phone_regex], max_length=15)
    signup = BooleanField(default=False)
    class Meta:
        model = CustomUser
        fields = ('mobile_number','signup')


def add_membership_id(user):
    if CustomUser.objects.count() == 0:
        user.membership_id = 1001
    else:
        latest_user_id = CustomUser.objects.latest('membership_id').membership_id
        user.membership_id = latest_user_id + 1

