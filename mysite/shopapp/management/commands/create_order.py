from typing import Sequence

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order, Product
from django.db import transaction


class Command(BaseCommand):
    """create command"""
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('create order with products')
        user = User.objects.get(username='kill_real')
        products: Sequence[Product] = Product.objects.all()
        order, created = Order.objects.get_or_create(
            delivery_adress='ul Ivanova 23',
            promocode='promo1',
            user=user,
        )
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(f'created order {order}')

