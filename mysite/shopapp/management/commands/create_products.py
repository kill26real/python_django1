from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    """creates command"""

    def handle(self, *args, **options):
        self.stdout.write('create products')

        product_names = [
            'Laptop',
            'Phone',
            'TV',
        ]
        for product_name in product_names:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f'created product {product.name}')


        self.stdout.write(self.style.SUCCESS('products created'))