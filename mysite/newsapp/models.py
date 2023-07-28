from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    text = models.TextField(default='', verbose_name='Содержимое')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True)
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    published = models.BooleanField(default=False)
    tag = models.CharField(max_length=30, verbose_name='Тэг', blank=True)

    class Meta:
        ordering = ['tag', 'published_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        permissions = {
            ('can_publish', 'Может публиковать')
        }

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)
    text = models.TextField(default='', verbose_name='Комментарий')
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    new = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        permissions = {
            ('can_publish', 'Может публиковать')
        }

    def __str__(self):
        if len(str(self.text)) < 48:
            return self.text
        return str(self.text)[:48] + '...'
