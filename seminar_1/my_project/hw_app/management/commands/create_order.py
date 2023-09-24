from django.core.management.base import  BaseCommand
from hw_app.models import Client, Order, Product


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("Client_id", type=int, help="Client ID")
        parser.add_argument('-p', '--Product_id', nargs='+', help="Client ID", required=True)

    def handle(self, *args, **kwargs):
        Client_id = kwargs.get('Client_id')
        Product_id: list = kwargs.get('Product_id')

        customer = Client.objects.filter(pk=Client_id).first()

        order = Order(customer=customer)
        total_price = 0
        for i in range(0, len(Product_id)):
            product = Product.objects.filter(pk=Product_id[i]).first()
            total_price += float(product.price)
            order.total_price = total_price
            order.save()
            order.products.add(product)