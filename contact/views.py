# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Internal:
from .forms import ContactForm
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def contact(request):
    """Display the contact form"""
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            send_auto_contact_received_email(contact_form)
            send_contact_notify_admin(contact_form)
            messages.success(request, 'Message sent, \
            please allow 1 working day for a response.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'There was an error sending your message \
                Please ensure all fields are valid and try again')
            return (request, 'contact/contact.html')

    else:
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'contact_name': user.default_full_name,
                    'contact_email': user.default_email,
                    'contact_phone_number': user.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
                send_auto_contact_received_email(contact_form)
                send_contact_notify_admin(contact_form)
        else:
            contact_form = ContactForm()
            send_auto_contact_received_email(contact_form)
            send_contact_notify_admin(contact_form)

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)


def send_auto_contact_received_email(contact_form):
    """Send the user a confirmation email"""
    if contact_form.is_valid():
        cust_email = contact_form.cleaned_data['contact_email']
        context = {
            'form_data': contact_form.cleaned_data,
            'contact_email': settings.DEFAULT_FROM_EMAIL,
        }
        subject = render_to_string(
            'contact_confirmation_emails/contact_confirmation_subject.txt',
            context
        )
        body = render_to_string(
            'contact_confirmation_emails/contact_confirmation_body.txt',
            context,
        )
        send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email],
            )


def send_contact_notify_admin(contact_form):
    """Send admin confirmation email of user contact"""
    if contact_form.is_valid():
        admin_email = settings.DEFAULT_FROM_EMAIL
        context = {
            'form_data': contact_form.cleaned_data,
            'contact_email': settings.DEFAULT_FROM_EMAIL,
        }
        subject = render_to_string(
            'contact_confirmation_emails/contact_admin_subject.txt',
            context
        )
        body = render_to_string(
            'contact_confirmation_emails/contact_admin_body.txt',
            context,
        )
        send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [admin_email],
            )


def contact_success(request):
    template = 'contact/contact_success.html'
    context = {
        'on_contact_page': True,
    }
    return render(request, template, context)
