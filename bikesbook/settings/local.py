from .base import *

DEBUG = True
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bikesbook',
        'HOST': '127.0.0.1',  # Or an IP Address that your DB is hosted on
        'PORT': '',
        'USER': 'root',
        'PASSWORD': '',
    }
}