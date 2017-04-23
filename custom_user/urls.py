"""customauth URL Configuration
"""
from django.conf.urls import url
from .views import home,login, loggedin, logout, invalid_login, register_user, register_success

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^loggedin/$', loggedin, name='loggedin'),
    url(r'^invalid/$', invalid_login, name='invalid'),
    url(r'^register/$', register_user, name='register'),
    url(r'^register_success/$', register_success, name='register_success'),
]
