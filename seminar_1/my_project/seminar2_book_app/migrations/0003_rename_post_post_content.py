# Generated by Django 4.2.5 on 2023-09-11 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2_book_app', '0002_category_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='content',
        ),
    ]