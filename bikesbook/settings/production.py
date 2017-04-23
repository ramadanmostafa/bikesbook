from .base import *


print "loading settings form production....."
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'bikesbook',
        # 'HOST': '127.0.0.1',  # Or an IP Address that your DB is hosted on
        # 'PORT': '',
        # 'USER': 'bikesbook',
        # 'PASSWORD': '7JuNWzGXfy',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bikesbook',
        'HOST': '127.0.0.1',  # Or an IP Address that your DB is hosted on
        'PORT': '',
        'USER': 'bikesbook',
        'PASSWORD': '123456',
    }
}
