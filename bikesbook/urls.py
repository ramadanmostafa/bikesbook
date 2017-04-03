"""bikesbook URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import refresh_jwt_token
from .views import home,contact,subscribe


def ssl_cert(request):

    from django.http import HttpResponse
    content = """39446B82DEF3ABD4DD1BF915247E12F9522EF3AA
comodoca.com"""
    return HttpResponse(content, content_type='text/plain')

urlpatterns = [
    url(r'^$', home, name='home_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/users/', include('custom_user.api.urls')),
    url(r'^api/garage/', include('garage.api.urls')),
    url(r'^api/ride/', include('ride.api.urls')),
    url(r'^api/places/', include('places.api.urls')),
    url(r'^api/schedule_ride/', include('schedule_ride.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-refresh/$', refresh_jwt_token),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^contact/$', contact, name='contact'),
    url(r'^subscribe/$', subscribe, name='subscribe'),
    url(r'^B120FBEBC59A1E29B57DE4B975FCB565.txt$', ssl_cert),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
