from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from garage.models import Garage
from custom_user.models import EmailConfirmed, CustomUser, Setting


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Garage.objects.create(user=instance)
        Setting.objects.create(user=instance)
        #if not user.is_social: pass
        # email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
        # if email_is_created:
        #     short_hash = hashlib.sha1(str(random.random())).hexdigest()[:5]
        #     base = user.email
        #     activation_key = hashlib.sha1(short_hash + base).hexdigest()
        #     email_confirmed.activation_key = activation_key
        #     email_confirmed.save()
        #     email_confirmed.activate_user_email()
