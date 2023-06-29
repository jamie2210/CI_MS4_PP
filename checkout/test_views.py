from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from checkout.models import Order
from profiles.models import UserProfile


class TestCheckoutViews(TestCase):
    """
    A class for testing checkout views
    """

    def test_get_checkout_with_empty_bag(self):
        """
        This tests for an empty cart for checkout
        """
        response = self.client.get('/checkout')
        self.assertTrue(response, '/products')

    def setUp(self):
        """
        Create test user and a test order
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        test_user.save()
        test_user = UserProfile.objects.get(user=test_user)

        Order.objects.create(
            full_name='Test User',
            email='test_email@gmail.com',
            phone_number='123456789',
            country='IE',
            town_or_city='Test City',
            street_address1='Test Address 1',
            street_address2='Test Address 2',
            user_profile=test_user
        )
