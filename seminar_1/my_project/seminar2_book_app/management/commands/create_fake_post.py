from django.core.management.base import BaseCommand
from seminar2_book_app.models import Post
from seminar2_book_app.models import Author
from seminar2_book_app.models import Category
import random



class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for c in Category.objects.all():
            for a in Author.objects.all():
                for i in range(1, count + 1):
                    post = Post(title=f'title{i}',
                                    content=f'content{i}',
                                    publish_date='2000-01-01',
                                    author=a,
                                    category=c,
                                    views=random.randint(1, 10),
                                    publish=random.randint(0, 1)
                    )
                    post.save()
