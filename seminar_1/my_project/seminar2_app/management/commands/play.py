from django.core.management.base import BaseCommand
from seminar2_app.models import GameModel
from random import randint

class Command(BaseCommand):
    help = "Play game Head and Tails."
    def handle(self, *args, **kwargs):
        result = ('TAILS', 'HEADS')[randint(0, 1)]
        game = GameModel(result=result)
        game.save()

        self.stdout.write(f'{game}')

