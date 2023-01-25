from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    text = models.TextField(default='', verbose_name='Содержимое')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)


    def text_short(self):
        if len(str(self.text)) < 100:
            return self.text
        return self.text[:100] + '...'


class Image(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name='Пост')
    img = models.ImageField(upload_to='files/')
