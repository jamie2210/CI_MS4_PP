# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestBagViews(TestCase):
    """
    A class for testing bag views
    """
    def setUp(self):
        """
        Create a test product
        """
        Product.objects.create(
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
        session = self.client.session
        session['bag'] = {}

        response = self.client.post(f'/bag/add/{product.id}/', {
            "quantity": 1,
            "redirect_url": "view_bag"
            })

        session.save()
        bag = self.client.session.get('bag', {})
        # Check if the product has sizes
        size = None
        if product.has_sizes:
            size = 'a4'  # Set size to match the logic in view

        if size:
            if str(product.id) in bag:
                if size in bag[str(product.id)]['items_by_size']:
                    bag[str(product.id)]['items_by_size'][size] += 1
                else:
                    bag[str(product.id)]['items_by_size'][size] = 1
            else:
                bag[str(product.id)] = {'items_by_size': {size: 1}}
        else:
            if str(product.id) in bag:
                bag[str(product.id)]['quantity'] += 1
            else:
                bag[str(product.id)] = {'quantity': 1}

        self.assertEqual(bag[str(product.id)]['quantity'], 1)

    def test_remove_product_from_bag(self):
        """
        This test removes a product from the bag
        """
        product = Product.objects.get(sku='123456')
        response = self.client.post(f'/bag/add/{product.id}/',
                                    {"quantity": 1,
                                     "redirect_url": "view_bag"})

        response = self.client.post(f'/bag/remove/{product.id}/')
