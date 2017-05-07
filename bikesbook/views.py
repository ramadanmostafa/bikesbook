from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from forms import ContactForm, SubscribeForm
from django.conf import settings
from django.shortcuts import get_object_or_404
from custom_user.models import Subscriber
import django
import json, urllib2, urllib

def privacy(request):
    return render(request, "privacy.html", {})

def home(request):
    # if request.user.is_authenticated() and request.user.is_staff:
    #     queryset = CustomUser.objects.all().order_by('-date_joined')
    #     context = {
    #         "queryset": queryset
    #     }
    # else:
    #     context = {"queryset": "welcome"}
    form = SubscribeForm()
    context = {
        "form": form,
    }
    return render(request, "bikes2017/index.html", context)


# add to your views
def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            import json, urllib2, urllib
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = json.load(response)
            ''' End reCAPTCHA validation '''
            if result['success']:
                form.save()
                # contact_name = request.POST.get('name', '')
                # contact_email = request.POST.get('email', '')
                # contact_subject = request.POST.get('subject', '')
                # form_content = request.POST.get('message', '')

                # Email the profile with the
                # contact information
                # template = get_template('contact_template.txt')
                # context = Context({
                #     'contact_name': contact_name,
                #     'contact_email': contact_email,
                #     'contact_subject': contact_subject,
                #     'form_content': form_content,
                #
                # })
                # content = template.render(context)
                # email = EmailMessage(
                #         contact_subject,
                #         content,
                #         "Bikes Book " + '',
                #         [settings.DEFAULT_FROM_EMAIL, "mhabdou76@gmail.com", "engsum@gmail.com"],
                #         headers={'Reply-To': contact_email}
                # )
                # email.send()
                messages.success(request, 'Your Mail has been sent')
                return redirect('/')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('contact')

    return render(request, 'bikes2017/contact.html', {'form': form_class,})


def subscribe(request):
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        # ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = json.load(response)
        # ''' End reCAPTCHA validation '''
        if result['success']:
            form.save()
            subscriber_email = request.POST.get('email', '')
            full_name = request.POST.get('full_name', '')
            # context = {
            #     'subscriber_email': subscriber_email,
            #     "full_name": full_name
            # }
            # message = render_to_string("accounts/subscriber_mail.txt", context)
            # subject = "Thank you for your subscription with bikesbook"
            # send_mail(
            #     subject,
            #     message,
            #     "Bikesbook <%s>" % settings.DEFAULT_FROM_EMAIL,
            #     [subscriber_email],
            #     fail_silently=True
            # )
            # redirect to the template
            #################################################################

            token = django.middleware.csrf.get_token(request)
            subscr = Subscriber.objects.get(email=subscriber_email)
            subscr.token = token
            subscr.save()
            activation_url = request.build_absolute_uri(
                django.core.urlresolvers.reverse(
                    'subs_validate_email',
                    kwargs={
                        "uidb64": subscr.pk,
                        "token": token
                    }
                )
            )
            ctx = {
                'name': full_name,
                'flag': True,
                'email': subscriber_email,
                'activationLink': activation_url,
                'openLink': activation_url
            }

            body = render_to_string('email/activation_email.html', ctx)

            subject = "email confirmation"
            send_mail(
                subject,
                body,
                "Bikesbook <%s>" % settings.DEFAULT_FROM_EMAIL,
                [subscriber_email, ""],
                fail_silently=True
            )
            ######################################################################
            messages.success(
                request,
                "Thank you, please click the link we just sent to your E-mail to complete the subscription."
            )
            return HttpResponseRedirect("/")
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please Insert Captcha to subscribe.')
            return redirect('/')
    else:
        context = {
        "form": form,
         }
    return render(request, "bikes2017/index.html", context)

def ssl_cert(request):

    from django.http import HttpResponse
    content = """39446B82DEF3ABD4DD1BF915247E12F9522EF3AA
comodoca.com"""
    return HttpResponse(content, content_type='text/plain')

def subs_validate_email(request, uidb64, token):

    subscriper = get_object_or_404(Subscriber, pk=uidb64, token=token)
    subscriper.confirmed = True
    subscriper.save()

    return render(request, 'email/email-confir.html', {})