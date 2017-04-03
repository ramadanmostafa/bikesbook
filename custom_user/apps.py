from __future__ import unicode_literals

from django.apps import AppConfig


class CustomUserConfig(AppConfig):
    name = 'custom_user'

    def ready(self):
        from custom_user import signals
