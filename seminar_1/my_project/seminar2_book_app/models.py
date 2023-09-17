from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    bd = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surname}, {self.email}, {self.bd}'


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} - {self.title} - {self.publish}'
