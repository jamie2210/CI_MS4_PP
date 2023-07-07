# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User

# Internal:
from .models import Favourites
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestFavouriteViews(TestCase):
    """
    A class for testing favourites Views
    """
    def setUp(self):
        """
        Create test user and favourite
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Favourites.objects.create(
            username=test_user
        )

    def test_get_product_favourites_page(self):
        """
        This test tests get the product favourites page
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/favourites/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favourites/favourites.html')

    def test_add_item_to_product_favourites(self):
        """
        This test adds a product to the users favourites list
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.create(
            name='Test Name',
            price='9.99',
            sku='123456',
            description='Test Description',
        )
        response = self.client.post(f'/favourites/add_to_favourites/'
                                    f'{product.id}/')

    def test_remove_item_from_favourites_in_favourites(self):
        """
        This test removes a product from the users favourites
        list from favourites page
        """
        test_user2 = User.objects.create_user(
            username='test_user2', password='test_password')
        self.client.login(username='test_user2', password='test_password')
        product = Product.objects.create(
            name='Test Name 2',
            price='9.99',
            sku='123456',
            description='Test Description',
        )
        product = Product.objects.get(name='Test Name 2')
        favourites = Favourites.objects.create(username=test_user2)
        favourites.products.add(product)
        redirect_from = 'favourites'
        response = self.client.get(
            f'/favourites/remove_from_favourites_in_favourites/'
            f'{product.id}/{redirect_from}/')

    def test_remove_item_from_favourites_in_products_detail(self):
        """
        This test removes a product from the users favourites
        list from product detail page
        """
        test_user3 = User.objects.create_user(
            username='test_user3', password='test_password')
        self.client.login(username='test_user3', password='test_password')
        product = Product.objects.create(
            name='Test Name 3',
            price='9.99',
            sku='123456',
            description='Test Description',
        )
        product = Product.objects.get(name='Test Name 3')
        favourites = Favourites.objects.create(username=test_user3)
        favourites.products.add(product)
        redirect_from = 'product_detail'
        response = self.client.get(
            f'/favourites/remove_from_favourites_in_products_detail/'
            f'{product.id}/{redirect_from}/')
