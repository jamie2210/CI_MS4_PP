from django.test import TestCase
from .forms import OrderForm


class TestCheckoutViews(TestCase):

    def test_get_checkout_with_empty_bag(self):
        """
        This tests for an empty cart for checkout
        """
        response = self.client.get('/checkout')
        self.assertTrue(response, '/products')
