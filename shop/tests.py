from django.test import TestCase

from shop.models import Product

class ProductModelTests(TestCase):
    products = Product.objects.get()
    price = products.price
    def test_price_is_a_positive_decimal(self):
        self.assertGreater(price>0, True)

    def test_price_decima(self):
        self.assertTrue(price, decimal)
