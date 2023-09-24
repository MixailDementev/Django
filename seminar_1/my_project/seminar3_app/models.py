from django.db import models
from django.urls import reverse


class Author(models.Model):

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} {self.create_date}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('posts_author', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.author} - {self.title} - {self.publish}'


