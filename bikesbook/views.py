from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template, render_to_string
from forms import ContactForm, SubscribeForm
from django.conf import settings


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

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            form.save()
            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            contact_subject = request.POST.get('subject', '')
            form_content = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'form_content': form_content,

            })
            content = template.render(context)
            email = EmailMessage(
                    contact_subject,
                    content,
                    "Bikes Book " + '',
                    [settings.DEFAULT_FROM_EMAIL, "mhabdou76@gmail.com", "engsum@gmail.com"],
                    headers={'Reply-To': contact_email}
            )
            email.send()
            messages.success(request, 'Your Mail has been sent')
            return redirect('/')

    return render(request, 'home.html', {'form': form_class,})


def subscribe(request):
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        form.save()
        subscriber_email = request.POST.get('email', '')
        full_name = request.POST.get('full_name', '')
        context = {
            'subscriber_email': subscriber_email,
            "full_name": full_name
        }
        message = render_to_string("accounts/subscriber_mail.txt", context)
        subject = "Thank you for your subscription with bikesbook"
        send_mail(
            subject,
            message,
            "Bikesbook <%s>" % settings.DEFAULT_FROM_EMAIL,
            [subscriber_email],
            fail_silently=True
        )
        messages.success(request, "Thank you for your interest an Email has been sent to you")
        return HttpResponseRedirect("/")
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