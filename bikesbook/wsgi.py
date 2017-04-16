"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
#
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bikesbook.settings.production")
#
# from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
#
# application = get_wsgi_application()
# application = DjangoWhiteNoise(application)

import os
import sys

path = '/var/www/bikesbook.bike/web/bikesbook'
if path not in sys.path:
    sys.path.append(path)
path += 'bikesbook'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bikesbook.settings.production'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()