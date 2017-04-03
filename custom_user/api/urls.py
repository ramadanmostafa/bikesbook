"""bikesbook URL Configuration
"""
from custom_user.api.views import (UserList, UserDetailAPIView, UserUpdateAPIView,SettingUpdateAPIView,UploadRide,
                                   UserCreateAPIView, FbCreateAPIView, ForgetPassword, ChangePassword, PasswordResetConfirmView,
                                   TwitterCreateAPIView, UploadAvatar, activation_view, chkactivation, reactivation,
                                   checkmobindb)
from django.conf.urls import url

# from rest_framework.authtoken import views

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
urlpatterns = [
    url(r'^$', UserList.as_view()),
    #url(r'^login/$', obtain_jwt_token),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^registerfb/$', FbCreateAPIView.as_view(), name='registerfb'),
    url(r'^registertwitter/$', TwitterCreateAPIView.as_view(), name='register_twitter'),
    url(r'^bikerdetails/$', UserDetailAPIView.as_view(), name='bikerdetails'),
    url(r'^updatebiker/$', UserUpdateAPIView.as_view(), name='updatebiker'),
    url(r'^updatesetting/$', SettingUpdateAPIView.as_view(), name='updatesetting'),
    url(r'^uploadavatar/$', UploadAvatar.as_view(), name='uploadavatar'),
    url(r'^uploadride/$', UploadRide.as_view(), name='uploadride'),
    url(r'^forgetpassword/$', ForgetPassword.as_view(), name='forgetpassword'),
    url(r'^changepassword/$', ChangePassword.as_view(), name='changepassword'),
    url(r'^activate/(?P<activation_key>\w+)/$', activation_view, name='activation_view'),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        name='reset_password_confirm'),
    url(r'^chkactivation/$', chkactivation.as_view(), name='chkactivation'),
    url(r'^reactivation/$', reactivation.as_view(), name='reactivation'),
    url(r'^checkmobindb/$', checkmobindb.as_view(), name='checkmobindb'),
]
