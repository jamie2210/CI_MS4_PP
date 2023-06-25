from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """
    A class for testing contact Forms
    """
    def test_contact_name_is_required(self):
        """
        A test to check whether the name
        field in the ContactForm is required.
        """
        form = ContactForm({'contact_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_name', form.errors.keys())
        self.assertEqual(
            form.errors['contact_name'][0], 'This field is required.')

    def test_contact_email_is_required(self):
        """
        A test to check whether the email
        field in the ContactForm is required.
        """
        form = ContactForm({'contact_email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_email', form.errors.keys())
        self.assertEqual(
            form.errors['contact_email'][0], 'This field is required.')

    def test_contact_subject_is_required(self):
        """
        A test to check whether the subject
        field in the ContactForm is required.
        """
        form = ContactForm({'contact_subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_subject', form.errors.keys())
        self.assertEqual(
            form.errors['contact_subject'][0], 'This field is required.')

    def test_contact_message_is_required(self):
        """
        A test to check whether the message
        field in the ContactForm is required.
        """
        form = ContactForm({'contact_message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_message', form.errors.keys())
        self.assertEqual(
            form.errors['contact_message'][0], 'This field is required.')

    def test_contact_phone_number_is_not_required(self):
        """
        A test to check whether the phone number
        field in the ContactForm is not required.
        """
        form = ContactForm(
            {
                'contact_name': 'Test Name',
                'contact_email': 'test@test.com',
                'contact_phone_number': '',
                'contact_subject': 'Test Subject',
                'contact_message': 'Test Message',
            })
        self.assertTrue(form.is_valid())
