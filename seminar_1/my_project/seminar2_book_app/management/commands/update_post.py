from django.core.management.base import BaseCommand
from seminar2_book_app.models import Post

class Command(BaseCommand):
    help = "Update post title by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('title', type=str, help='post title')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        title = kwargs.get('title')
        content = Post.objects.filter(pk=pk).first()
        content.title = title
        content.save()
        self.stdout.write(f'{content}')