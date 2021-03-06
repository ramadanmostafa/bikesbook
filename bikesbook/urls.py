"""bikesbook URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import refresh_jwt_token
from .views import home, contact, subscribe, ssl_cert, subs_validate_email, privacy




urlpatterns = [
    url(r'^$', home, name='home_page'),
    url(r'^subscribe/validate_email/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]+)/$',
            subs_validate_email,
            name='subs_validate_email'
        ),
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
    url(r'^privacy/$', privacy, name='privacy'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
