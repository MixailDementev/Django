from django.core.management.base import BaseCommand
from hw_app.models import Client
import radar


class Command(BaseCommand):
    help = "Create fake client."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name_{i}',
                            phone=f'phone-{i}',
                            email=f'email{i}@example.com',
                            address=f'City_{i}',
                            date_registration=radar.random_datetime(start='2010-05-24', stop='2023-05-24')
                            )
            client.save()
