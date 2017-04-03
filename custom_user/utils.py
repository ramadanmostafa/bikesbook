import cookielib
import random
import urllib2

from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.conf import settings


# enhancment get max num of requests per user
def _get_pin(length=4):
    """ Return a numeric PIN with length digits """
    return random.sample(range(10 ** (length - 1), 10 ** length), 1)[0]


def send_sms(send_sms_url, send_sms_data):
    if settings.SEND_SMS:

        # For Cookies:
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        # Adding Header detail:
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

        try:
            opener.open(send_sms_url, send_sms_data)

        except IOError:
            return Response({"code": "IOError"}, status=HTTP_400_BAD_REQUEST)
