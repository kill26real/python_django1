from django.test import TestCase
from django.urls import reverse
from shopapp.models import Order, Sale, Offer, Product
from django.contrib.auth.models import User


class AccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_id = 0
        product = Product.objects.create(name='test product', description='test descr', price=100)
        Sale.objects.create(text='test text', user_id=user_id)
        Offer.objects.create(text='test text', user_id=user_id)
        Order.objects.create(delivery_adress='test address', promocode='test', user_id=user_id, products=product)

    def test_order_list(self, user_id):
        response = self.client.get(f'/user/{user_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userapp/account.html')

    def test_user_forbidden_other_users(self):
        response = self.client.get(f'/user/1/')
        self.assertEqual(response.status_code, 403)


    def test_user_forbidden_update_other_users(self):
        response = self.client.get(f'/user/1/update_user')
        self.assertEqual(response.status_code, 403)


    def test_user_forbidden_update_other_users_profiles(self):
        response = self.client.get(f'/user/1/update_user')
        self.assertEqual(response.status_code, 403)

