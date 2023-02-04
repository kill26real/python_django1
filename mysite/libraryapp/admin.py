from django.contrib import admin
from .models import Author, Book


class BookInline(admin.StackedInline):
    model = Author.books.through


class AuthorInline(admin.StackedInline):
    model = Book.author.through


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [
        AuthorInline,
    ]
    list_display = 'name', 'description', 'ibsn', 'pages', 'created_at'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
    list_display = 'name', 'surname', 'birthday'
