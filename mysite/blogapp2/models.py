from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=False, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=40)

class Tag(models.Model):
    name = models.CharField(max_length=20)


class Article(models.Model):
    class Meta:
        ordering = ['pub_date', 'title']

    title = models.CharField(max_length=200)
    content = models.TextField(default='no content')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    archivated = models.BooleanField(default=False)

    def __str__(self):
        return f'Article # (pk={self.pk}, title:{self.title}'
