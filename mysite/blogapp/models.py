from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class BlogPost(models.Model):
    text = models.TextField(default='', verbose_name=_('text'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('author'))
    published_at = models.DateTimeField(verbose_name=_('date of publish'), auto_now_add=True)
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


    def text_short(self):
        if len(str(self.text)) < 100:
            return self.text
        return self.text[:100] + '...'


class Image(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name=_('post'))
    img = models.ImageField(upload_to='files/', verbose_name=_('image'))
    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
