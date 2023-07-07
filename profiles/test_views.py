# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User

# Internal:
from checkout.models import Order
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProfileViews(TestCase):

    def setUp(self):
        """
        This setup creates a test user,
        test product and test order
        """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com')
        testuser.save()

        Order.objects.create(
            order_number='12345678',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='test@test.com',
            phone_number='12345678',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

    def test_get_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (get)
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (post)
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.post('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_order_detail_page(self):
        """
        This test logins a test user and accesses
        the order history page for a test order
        """
        self.client.login(username='test_user', password='test_password')
        test_user = User.objects.get(username='test_user')
        order = Order.objects.get(email=test_user.email)
        response = self.client.get(
            '/profile/order_history/' + order.order_number)
        self.assertEqual(response.status_code, 200)
