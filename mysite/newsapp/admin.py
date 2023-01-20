from django.contrib import admin
from .models import News, Comment



class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user']


admin.site.register(News, NewsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user']


admin.site.register(Comment, CommentAdmin)

