from django.core.management.base import BaseCommand
from shop.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate the database with sample honey and bee products'

    def handle(self, *args, **kwargs):
        # Clear existing products
        Product.objects.all().delete()

        # Create sample products
        products = [
            {
                'name': 'Honey',
                'variant': 'Pint',
                'description': 'Pure, raw honey from our local hives. Perfect for sweetening tea, baking, or enjoying straight from the jar.',
                'price': Decimal('14.00'),
                'stock': 50,
                'rating': 5.0
            },
            {
                'name': 'Honey',
                'variant': 'Quart',
                'description': 'Bulk honey perfect for families or those who use honey regularly. Fresh from our apiary to your table.',
                'price': Decimal('24.00'),
                'stock': 40,
                'rating': 5.0
            },
            {
                'name': 'Honey',
                'variant': 'Gallon',
                'description': 'Our premium gallon size for serious honey lovers. Great for large families or small businesses.',
                'price': Decimal('85.00'),
                'stock': 20,
                'rating': 4.9
            },
            {
                'name': 'Pure Beeswax',
                'variant': '1 lb Block',
                'description': 'Raw beeswax block for candle making, lip balms, and other DIY projects. 100% natural.',
                'price': None,
                'stock': 15,
                'rating': 4.8
            },
            {
                'name': 'Beeswax Candles',
                'variant': 'Singles',
                'description': 'Hand-poured beeswax candles with natural honey scent. Clean burning and long-lasting.',
                'price': None,
                'stock': 25,
                'rating': 5.0
            },
        ]

        # Create products
        for product_data in products:
            Product.objects.create(**product_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(products)} products'))
