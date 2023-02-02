from django.test import TestCase
from django.urls import reverse
from shopapp.models import Order, Shop, Product


NUMDER_OF_ITEMS = 5


class OrderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(NUMDER_OF_ITEMS):
            product = Product.objects.create(name='test product', description='test descr', price=i*10, )
            products = Product.objects.filter(name='test product')
            Order.objects.create(delivery_adress='test address', promocode='test', user_id=0 , products=products)

    def test_order_list(self):
        response = self.client.get('/shop/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopapp/order_list.html')

    def test_numbers_posts(self):
        response = self.client.get(reverse('orders-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['Order_list']) == 5)


class ShopTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(NUMDER_OF_ITEMS):
            product = Product.objects.create(name='test product', description='test descr', price=i*10, )
            products = Product.objects.filter(name='test product')
            Shop.objects.create(adress='test address', description='test descr', name='test name' , products=products)

    def test_shop_list(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopapp/shop-index.html')

    def test_numbers_posts(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['Shop_list']) == 5)
