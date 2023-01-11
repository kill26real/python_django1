from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order



class Command(BaseCommand):
    """creates command"""

    def handle(self, *args, **options):
        self.stdout.write('create order')
        user = User.objects.get(username='kill_real')
        order = Order.objects.get_or_create(
            delivery_adress='ul Pupkina',
            promocode='SALE123',
            user=user,
        )
        self.stdout.write(f'created order {order}')

