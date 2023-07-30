from django.contrib import admin
from .models import Author, Tag, Article, Category
from django.http import HttpRequest
from django.db.models import QuerySet


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']



class ArticleTagsInline(admin.TabularInline):
    model = Article.tags.through


@admin.action(description='Archive articles')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archivated=True)


@admin.action(description='Unarchive articles')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archivated=False)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        mark_unarchived,
    ]
    inlines = [
        ArticleTagsInline,
    ]
    list_display = 'pk', 'title', 'content', 'pub_date', 'author', 'category',  'archivated'
    list_display_links = 'pk', 'title'


    def description_short(self, obj: Article):
        if len(obj.content) < 48:
            return obj.content
        return obj.content[:48] + '...'
