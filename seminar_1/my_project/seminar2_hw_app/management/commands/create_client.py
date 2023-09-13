from django.core.management.base import BaseCommand
from seminar2_hw_app.models import Client

class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
            client = Client(name='Jack',
                        phone='+79115559988',
                        email='capitan@example.com', address='Moscow, Kremlin',
                        date_registration='2022-09-05')
            client.save()
            self.stdout.write(f'{client}')