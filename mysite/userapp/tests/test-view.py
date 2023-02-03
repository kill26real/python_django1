from django.test import TestCase
from django.urls import reverse
from shopapp.models import Order, Sale, Offer, Product


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
    # TODO 1) провеьте что пользователь не может просматривать чужие профили и не может их изменять (что выбрасывается
    #  PermissionError)
