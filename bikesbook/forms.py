from custom_user.models import Contact,Subscriber
from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['full_name', 'email', 'country']
        widgets = {'country': CountrySelectWidget()}
