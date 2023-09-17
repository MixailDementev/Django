from django.core.management.base import BaseCommand

from seminar2_book_app.models import Post


class Command(BaseCommand):
    help = "Get post."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        content = Post.objects.get(pk=pk)

        self.stdout.write(f'{content}')

