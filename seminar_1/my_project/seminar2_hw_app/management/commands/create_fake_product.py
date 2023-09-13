import random
import radar
from django.core.management.base import BaseCommand
from seminar2_hw_app.models import Product, Client


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'product{i}',
                              description=f'description{i}',
                              price=random.randrange(100, 10000),
                              quantity=random.randint(1, 100),
                              date_add=radar.random_datetime(start='2020-05-24', stop='2023-05-24'))
            product.save()

