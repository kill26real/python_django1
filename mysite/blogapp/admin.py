from django.contrib import admin
from .models import BlogPost, Image


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['text', 'user']
