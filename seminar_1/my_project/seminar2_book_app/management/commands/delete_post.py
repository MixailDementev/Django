from django.core.management.base import BaseCommand
from seminar2_book_app.models import Post

class Command(BaseCommand):
    help = "Delete post title by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        content = Post.objects.filter(pk=pk).first()
        if content is not None:
            content.delete()
        self.stdout.write(f'Deleted {content}')
