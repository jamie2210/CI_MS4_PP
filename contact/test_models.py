from django.test import TestCase
from .models import ContactForm


class TestContactModels(TestCase):
    """
    A class for testing contact models
    """
    def test_string_representation(self):
        # Create a ContactForm instance with a specific contact email
        contact = ContactForm(contact_email="test@email.com")
        self.assertEqual(str(contact), contact.contact_email)

    def test_replied_defaults_to_false(self):
        # Create a contact form
        contact_form = ContactForm.objects.create(
            contact_name="mr test",
            contact_email="test@test.com",
            contact_phone_number="123345",
            contact_message="test message",
        )
        # Replied field of the ContactForm is False by default
        self.assertFalse(contact_form.replied)
