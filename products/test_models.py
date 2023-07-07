# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from products.models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user', password="test_password")

        Category.objects.create(
            name='test_category', friendly_name='test category'
        )

        product = Product.objects.create(
            name='Test Name',
            price='9.99',
            sku='123456',
            description='Test Description',
        )

    def test_product_str_method(self):
        """
        This test tests the products str method
        """
        product = Product.objects.get(sku='123456')
        self.assertEqual((product.__str__()), product.name)

    def test_category_str_method(self):
        """
        This test tests the categories str method
        """
        category = Category.objects.get(name='test_category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(
            category.get_friendly_name(), category.friendly_name)
