import order as order
from django.core.management.base import BaseCommand
from seminar2_hw_app.models import Client, Product, Order
from django.utils.timezone import datetime

import random
class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('client', type=int, help='client ID')
        parser.add_argument('product', type=int, help='product ID')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs.get('client'))
        products = Product.objects.get(pk=kwargs.get('product'))

        order = Order(customer=client,

                    total_price = products.price,
                    date_ordered=datetime.now()
                    )
        order.save()


        self.stdout.write(f'done, order pk = {order.pk}')


