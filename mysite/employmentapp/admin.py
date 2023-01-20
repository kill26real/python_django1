from django.contrib import admin

from .models import Vacancy, Resume


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Resume, ResumeAdmin)
