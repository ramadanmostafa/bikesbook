"""customauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
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
