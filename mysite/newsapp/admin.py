from django.contrib import admin
from .models import News, Comment
from django.contrib import admin
from .models import News, Comment
from django.http import HttpRequest
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.models import Group



# my_group = Group.objects.get(name='Пользователи')
# my_group.user_set.add(user)


# class NewsInline(admin.TabularInline):
#     model = News.user.through


# @admin.action(description='Verify user')
# def mark_verified(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
#     queryset.update(is_verificied=True)


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     actions = [
#         mark_verified,
#     ]
#     list_display = ['id', 'title', 'user']
#     search_fields = ['first_name', 'last_name', 'date_of_birth', 'city', 'phone_number', 'is_verificied', 'news']

@admin.action(description='publish news')
def mark_published(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(published=True)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user']
    actions = [mark_published,]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user']

