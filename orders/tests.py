from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from cart.cart import Cart

from . import views

cart = Cart

class CartCreationTest(TestCase):
    
    def test_cart_creation_status_code(self):
        response = self.client.get('/orders/create/')
        self.assertEquals(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('order_create'))
        self.assertEquals(response.status_code, 200)


    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('order_create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order/create.html')