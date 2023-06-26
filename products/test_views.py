from django.test import TestCase
from .models import Category, Product
from django.contrib.auth.models import User
from django.test.client import Client


class TestProductViews(TestCase):
    """
    A class for testing product views
    """
    def setUp(self):
        """
        Create test product
        """
        Product.objects.create(
            name='Test Name',
            price='9.99',
            sku='123456',
            description='Test Description',
        )

    def test_get_products_page(self):
        """
        This test tests get product page
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_products_detail_page(self):
        """
        This test tests get product details page
        """
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/',
                                   {'product': product, })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_add_product_page_user(self):
        """
        This test tests get product add page as aregular user
        """
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    def test_get_edit_product_page_user(self):
        """
        This test tests edit product add page as aregular user
        """
        product_id = 1
        response = self.client.get(f'/products/edit/{product_id}/')
        self.assertEqual(response.status_code, 302)

    def test_add_product_as_superuser(self):
        """
        This test tests add product page as a superuser
        """
        User.objects.create_superuser(
            username='test_super_user', password='test_password')
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_edit_product_as_superuser(self):
        """
        This test tests edit product page as a superuser
        """
        User.objects.create_superuser(
            username='test_super_user', password='test_password')
        self.client.login(username='test_super_user', password='test_password')
        product_id = 1
        response = self.client.get(f'/products/edit/{product_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
