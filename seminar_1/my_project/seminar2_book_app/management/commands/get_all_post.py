from django.core.management.base import BaseCommand

from seminar2_book_app.models import Post


class Command(BaseCommand):
    help = "Get all posts."

    def handle(self, *args, **kwargs):
        content = Post.objects.all()

        self.stdout.write(f'{content}')

