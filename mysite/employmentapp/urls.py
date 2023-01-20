from django.urls import path
from .views import vacancy_list

urlpatterns = [
    path('vac/', vacancy_list, name='vacancy-list'),
]