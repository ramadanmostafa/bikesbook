import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField

now = datetime.datetime.now()
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = datetime.datetime.now()

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        return self._create_user("temp@int.com", password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=254, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=254, blank=True)
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=254, blank=True)
    area_code = models.CharField(max_length=20, blank=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    avatar = models.ImageField('profile picture', upload_to='avatar/%Y/%m', null=True, blank=True)
    ridefile = models.FileField(null=True,blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_social = models.BooleanField(default=False)
    fb_id = models.CharField(max_length=60, blank=True, null=True, unique=True)
    twitter_id = models.CharField(max_length=60, blank=True, null=True, unique=True)
    membership_id = models.BigIntegerField(unique=True, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    pin_code = models.CharField(max_length=4)
    # is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        return unicode(self.mobile_number)


class EmailConfirmed(models.Model):
    user = models.OneToOneField(CustomUser)
    activation_key = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.confirmed)

    def activate_user_email(self):
        # send email here & render a string
        activation_url = "%s%s" % (settings.SITE_URL, reverse("activation_view", args=[self.activation_key]))
        context = {
            "activation_key": self.activation_key,
            "activation_url": activation_url,
            "email": self.user.email,
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activate your Email"
        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.user.email], fail_silently=True)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    message_date = models.DateTimeField(_('message date'), default=timezone.now)

    def __unicode__(self):
        return self.name


class Setting(models.Model):
    user = models.OneToOneField(CustomUser)
    Allow_bikers_join = models.BooleanField(default=False)
    get_sos_notifications = models.BooleanField(default=False)
    gps_acc = models.CharField(max_length=60, default='30')
    distance_unit = models.CharField(max_length=60, default='km')
    connect_with_fb = models.BooleanField(default=False)
    connect_with_twitter = models.BooleanField(default=False)
    publish_time_interval = models.CharField(max_length=60, default='30')
    share_my_info_using = models.CharField(max_length=60)

    def __unicode__(self):
        return self.gps_acc


class Subscriber(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    country = CountryField(blank_label='(select country)')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    def __unicode__(self):
        return self.full_name

