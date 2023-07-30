from django.db import models
from datetime import datetime


class Author(models.Model):
    """Модель автора."""
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateTimeField(null=False, blank=False)


class Book(models.Model):
    """Модель книги."""
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name='books')
    description = models.TextField(null=False, blank=True)
    ibsn = models.IntegerField(default=0)
    pages = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

