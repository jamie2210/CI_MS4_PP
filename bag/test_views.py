from django.test import TestCase
from products.models import Product


class TestBagViews(TestCase):
    """
    A class for testing bag views
    """
    def setUp(self):
        self.setUpProduct()

    def setUpProduct(self):
        """
        Create a test product
        """
        product = Product.objects.create(
            name='Test Name',
            price='9.99',
            sku='123456',
            description='This is a test description',
            stock='5',
        )

    def test_get_bag_page(self):
        """
        This test checks that the bag page is displayed
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_product_to_bag(self):
        """
        This test adds a product to the bag
        """
        product = Product.objects.get(sku='123456')
        self.client.session['bag'] = {}
        response = self.client.post(f'/bag/add/{product.id}/',
                                    {"quantity": 1,
                                     "redirect_url": "view_bag"})

        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)

    def test_remove_product_from_bag(self):
        """
        This test removes a product from the bag
        """
        product = Product.objects.get(sku='123456')
        response = self.client.post(f'/bag/add/{product.id}/',
                                    {"quantity": 1,
                                     "redirect_url": "view_bag"})

        bag = self.client.session['bag']
        response = self.client.post(f'/bag/remove/{product.id}/')
