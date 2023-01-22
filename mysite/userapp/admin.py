from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .models import Profile


@admin.action(description='verify user')
def mark_verified(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_verificied=True)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    actions = [
        mark_verified,
    ]
    list_display = 'user', 'city', 'date_of_birth', 'phone_number', 'is_verificied', 'news'
    list_display_links = 'user',
