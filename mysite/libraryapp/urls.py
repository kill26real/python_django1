from django.urls import path
from .views import AuthorList, BookList


app_name = 'libraryappapp'
urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors-list'),
    path('books/', BookList.as_view(), name='books-list'),
]