# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from products.models import Product
from poster_prints import settings
from .models import Order
from .models import OrderLineItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestFavouriteModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create test users, product and order
        """

        Product.objects.create(
            name='Test Name',
            price='9.99',
            sku='123456',
            description='Test Description',
        )

        Order.objects.create(
            full_name='mr test',
            email='test@test.com',
            phone_number='123345',
            country='GB',
            town_or_city='Test City',
            street_address1='Test Street',
        )

    def test_order_str_method(self):
        """
        This test tests the order str method
        """
        order = Order.objects.get(email='test@test.com')
        self.assertEqual(str(order), order.order_number)
