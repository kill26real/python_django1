from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    text = models.TextField(default='', verbose_name='Содержимое')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    img = models.ImageField(upload_to='feles/')

