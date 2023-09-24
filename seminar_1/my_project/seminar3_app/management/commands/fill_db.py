from random import choices, randint, choice

import radar
from django.core.management.base import BaseCommand
from django.db.models.functions import datetime
from seminar3_app.models import Author, Post, Comment


LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime " \
        "nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(
                name=f'Name_{i}',
                surname=f'Surname_{i}',
                email=f'email_{i}@mail.ru',
                biography=" ".join(choices(text, k=randint(1, 100))),
                birthday=radar.random_datetime(start='1910-05-24', stop='2010-05-24')
            )
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=f'Text from {author.name}',
                    publish_date=radar.random_datetime(start='2000-05-24', stop='2023-05-24'),
                    author=author,
                    views=randint(1, 1000),
                    publish=choice([True, False])
                )
                post.save()


