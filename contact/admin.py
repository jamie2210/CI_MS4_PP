from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = (
        'contact_name',
        'contact_email',
        'contact_phone_number',
        'contact_subject',
        'contact_message',
        'date',
    )

    fields = (
        'contact_name',
        'contact_email',
        'contact_phone_number',
        'contact_subject',
        'contact_message',
    )

    list_display = (
        'contact_phone_number',
        'contact_subject',
        'date',
    )

    ordering = ('-date',)


admin.site.register(ContactForm, ContactFormAdmin)
